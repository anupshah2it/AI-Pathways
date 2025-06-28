from abc import ABC, abstractmethod
from typing import Any, Dict

class BaseAdapter(ABC):
    """Base class for all adapters."""

    def __init__(self, config: Dict[str, Any]):
        self.config = config

    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def send(self, message: Any) -> None:
        pass

    @abstractmethod
    def receive(self) -> Any:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
