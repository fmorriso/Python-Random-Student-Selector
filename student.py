from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Student():
    first_name: str
    last_name: str
    period: int
