from abc import ABC, abstractmethod


class Clothes(ABC):
    name: str

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def calculate_consumption(self):
        pass


class Coat(Clothes):
    V: int

    def __init__(self, name: str, v: int):
        super().__init__(name)
        self.V = v

    @property
    def calculate_consumption(self):
        return round(self.V / 6.5 + 0.5, 2)


class Suit(Clothes):
    H: int

    def __init__(self, name: str, h: int):
        super().__init__(name)
        self.H = h

    @property
    def calculate_consumption(self):
        return round(self.H * 2 + 0.3, 2)


user_coat = Coat("Channel", 150)
print(f"Coat material consumption: {user_coat.calculate_consumption}")

user_suit = Suit("Gucci", 185)
print(f"Suit material consumption: {user_suit.calculate_consumption}")

print(f"Total material consumption: {user_coat.calculate_consumption + user_suit.calculate_consumption}")
