import json
import subprocess
from typing import Any
from .base import BaseTranslator

class JsTranslator(BaseTranslator):
    """Translator that executes a JS file to transform messages."""
    def __init__(self, script_path: str):
        self.script_path = script_path

    def translate(self, message: Any) -> Any:
        process = subprocess.run(
            ["node", self.script_path],
            input=json.dumps(message).encode(),
            stdout=subprocess.PIPE,
            check=True,
        )
        return json.loads(process.stdout.decode())
