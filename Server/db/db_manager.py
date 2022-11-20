from abc import ABC, abstractmethod
from typing import List, Dict
from db.objects import User, Category, Transaction


class DataBaseManager(ABC):

    # transactions operations
    @abstractmethod
    def add_transaction(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def delete_transaction(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    def get_all_transactions(self) -> List[Transaction]:
        pass

    # users operations
    @abstractmethod
    def add_user(self, user: User) -> None:
        pass

    @abstractmethod
    def get_balance(self, user_id: int) -> float:
        pass

    # categories operations
    @abstractmethod
    def add_category(self, category: Category) -> None:
        pass

    @abstractmethod
    def get_all_categories(self) -> List[Category]:
        pass

    # other operations
    @abstractmethod
    def get_breakdown_by_categories(self) -> Dict[str, float]:
        pass
