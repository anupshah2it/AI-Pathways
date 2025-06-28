from adapters.mock import MockAdapter


def test_mock_adapter_send_receive():
    adapter = MockAdapter({})
    adapter.connect()
    adapter.send({"hello": "world"})
    adapter.received.append({"foo": "bar"})
    msg = adapter.receive()
    assert msg == {"foo": "bar"}
    adapter.close()
