from dataclasses import dataclass

@dataclass
class IntValue:
    value: int

    def __repr__(self):
        return f"{self.value}"

@dataclass
class FloatValue:
    value: float

    def __repr__(self):
        return f"{self.value}"
        