from dataclasses import dataclass
from typing import Optional, Any


@dataclass
class GenericContext:
    event_id: Optional[str]
    raw_context: Any
