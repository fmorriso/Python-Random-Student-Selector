from dataclasses import dataclass, field
from typing import Optional

from dataclasses_json import dataclass_json

@dataclass_json
@dataclass(unsafe_hash=True)
class Student():
    last_name: str
    first_name: str
    period: int
    absent: Optional[bool] = field(default=False)

