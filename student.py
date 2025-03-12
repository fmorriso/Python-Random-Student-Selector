from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass(unsafe_hash=True)
class Student():
    first_name: str
    last_name: str
    period: int
