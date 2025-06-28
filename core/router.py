import json
import threading
import time
from importlib import import_module
from typing import Dict, Any, List
from .channel import Channel

class Router:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.channels: List[Channel] = []
        self.adapters: Dict[str, Any] = {}
        self.load_config()
        self.running = False
        self.thread: threading.Thread | None = None

    def load_config(self) -> None:
        with open(self.config_path) as f:
            data = json.load(f)
        self.channels = [Channel(**c) for c in data.get("channels", [])]

    def reload_config(self) -> None:
        """Reload configuration at runtime."""
        self.load_config()

    def start(self) -> None:
        self.running = True
        self.thread = threading.Thread(target=self.run, daemon=True)
        self.thread.start()

    def stop(self) -> None:
        self.running = False
        if self.thread:
            self.thread.join()

    def _get_adapter(self, conf: Dict[str, Any]) -> Any:
        key = conf["type"]
        if key not in self.adapters:
            module = import_module(f"adapters.{key}")
            cls = getattr(module, conf.get("class", key.title() + "Adapter"))
            self.adapters[key] = cls(conf)
        return self.adapters[key]

    def _get_translator(self, conf: Dict[str, Any]) -> Any:
        if not conf:
            return None
        module = import_module(f"translators.{conf['type']}")
        cls = getattr(module, conf.get("class", conf['type'].title() + "Translator"))
        return cls(**{k: v for k, v in conf.items() if k not in ["type", "class"]})

    def run(self) -> None:
        while self.running:
            for channel in self.channels:
                source = self._get_adapter(channel.source)
                dest = self._get_adapter(channel.destination)
                translator = self._get_translator(channel.translator)
                source.connect()
                dest.connect()
                try:
                    msg = source.receive()
                    if msg is None:
                        continue
                    if translator:
                        msg = translator.translate(msg)
                    dest.send(msg)
                finally:
                    source.close()
                    dest.close()
            time.sleep(1)
