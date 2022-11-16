class User:
    id = 0

    def __init__(self, name: str, balance: float, id: int = None) -> None:
        self.id = id if id is not None else User.id
        self.name = name
        self.balance = balance
        User.id += 1
