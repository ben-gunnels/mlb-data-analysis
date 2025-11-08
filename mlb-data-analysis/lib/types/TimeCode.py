import re
from dataclasses import dataclass

@dataclass(frozen=True)
class TimeCode:
    value: str

    _pattern = re.compile(r"^\d{8}_\d{6}$")

    def __post_init__(self):
        if not self._pattern.match(self.value):
            raise ValueError(
                f"Invalid timecode format: {self.value}. Expected YYYYMMDD_HHMMSS (UTC)."
            )

    def to_datetime(self):
        from datetime import datetime
        return datetime.strptime(self.value, "%Y%m%d_%H%M%S")