class Category:
    id = 0

    def __init__(self, name: str, id: int = None) -> None:
        self.id = id if id is not None else Category.id
        self.name = name
        Category.id += 1
