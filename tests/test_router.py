import json
import time
from core.router import Router
from adapters.mock import MockAdapter


def test_router_flow(tmp_path, monkeypatch):
    config = tmp_path / "channels.json"
    data = {
        "channels": [
            {
                "name": "c1",
                "source": {"type": "mock"},
                "destination": {"type": "mock"},
                "translator": {"type": "js", "script_path": "translators/sample.js"},
            }
        ]
    }
    config.write_text(json.dumps(data))
    router = Router(str(config))

    # Replace adapters with MockAdapter instances sharing state
    source = MockAdapter({})
    dest = MockAdapter({})
    router.adapters = {}

    def get_adapter(conf):
        return dest if conf is router.channels[0].destination else source

    router._get_adapter = get_adapter

    source.received.append({"foo": "bar"})
    router.start()
    time.sleep(0.1)
    router.stop()

    assert dest.sent == [{"wrapped": {"foo": "bar"}}]
