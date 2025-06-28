from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class Channel:
    name: str
    source: Dict[str, Any]
    destination: Dict[str, Any]
    translator: Dict[str, Any] = field(default_factory=dict)
    retries: int = 3
    alerts: Dict[str, Any] = field(default_factory=dict)
