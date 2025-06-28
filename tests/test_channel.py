from core.channel import Channel


def test_channel_init():
    data = {
        "name": "test",
        "source": {"type": "mock"},
        "destination": {"type": "mock"},
        "translator": {"type": "js", "script_path": "translators/sample.js"},
        "retries": 2,
    }
    c = Channel(**data)
    assert c.name == "test"
    assert c.retries == 2
