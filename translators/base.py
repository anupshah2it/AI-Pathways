from abc import ABC, abstractmethod
from typing import Any

class BaseTranslator(ABC):
    """Base class for translators."""

    @abstractmethod
    def translate(self, message: Any) -> Any:
        pass
