import re
from dataclasses import dataclass

@dataclass(frozen=True)
class Date:
    value: str

    _pattern = re.compile(r"^\d{4}-\d{2}-\d{2}$")

    def __post_init__(self):
        if not self._pattern.match(self.value):
            raise ValueError(
                f"Invalid date format: {self.value}. Expected YYYY-MM-DD."
            )