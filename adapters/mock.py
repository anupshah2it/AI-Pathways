from typing import Any, Dict, List
from .base import BaseAdapter

class MockAdapter(BaseAdapter):
    """Simple adapter for testing purposes."""
    def __init__(self, config: Dict[str, Any]):
        super().__init__(config)
        self.sent: List[Any] = []
        self.received: List[Any] = []
        self.connected = False

    def connect(self) -> None:
        self.connected = True

    def send(self, message: Any) -> None:
        if not self.connected:
            raise RuntimeError("Adapter not connected")
        self.sent.append(message)

    def receive(self) -> Any:
        if not self.connected:
            raise RuntimeError("Adapter not connected")
        if self.received:
            return self.received.pop(0)
        return None

    def close(self) -> None:
        self.connected = False
