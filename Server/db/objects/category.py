class Category:
    id = 0

    def __init__(self, name: str) -> None:
        self.id = Category.id
        self.name = name
        Category.id += 1
