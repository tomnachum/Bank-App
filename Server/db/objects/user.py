class User:
    id = 0

    def __init__(self, name: str, balance: float) -> None:
        self.id = User.id
        self.name = name
        self.balance = balance
        User.id += 1
