from abc import ABC, abstractmethod
from objects.user import User
from objects.category import Category
from objects.transaction import Transaction


class dbManager(ABC):
    @abstractmethod
    def add_user(self, user: User):
        pass

    @abstractmethod
    def add_category(self, category: Category):
        pass

    @abstractmethod
    def add_transaction(self, transaction: Transaction):
        pass
