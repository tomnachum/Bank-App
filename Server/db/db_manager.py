from abc import ABC, abstractmethod
from objects.user import User
from objects.category import Category
from objects.transaction import Transaction
from typing import List, Dict


class DataBaseManager(ABC):
    @abstractmethod
    def add_user(self, user: User) -> None:
        pass

    @abstractmethod
    def add_category(self, category: Category) -> None:
        pass

    @abstractmethod
    def add_transaction(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def get_all_transactions(self) -> List[Transaction]:
        pass

    @abstractmethod
    def delete_transaction(self, transaction_id: int) -> None:
        pass

    @abstractmethod
    def get_breakdown_by_categories(self) -> Dict[str, float]:
        pass
