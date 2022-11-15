from objects.user import User
from objects.category import Category
from objects.transaction import Transaction
from utils.connection import get_connection_to_db
import queries.categories_queries as categories_queries
import queries.transactions_queries as transactions_queries
import queries.users_queries as users_queries
from db_manager import DataBaseManager
from objects.raw_data_to_object import extract_transaction
from typing import List, Dict
import utils.constants as c


class MySqlManager(DataBaseManager):
    def __init__(self, db_name) -> None:
        """
        This class assumes that the DB is already created.
        """
        self.connection = get_connection_to_db(db_name)
        self.connection.autocommit(True)

    def _execute_query(self, query):
        self.connection.ping()
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    def add_user(self, user: User) -> None:
        query = users_queries.insert_into_users(user)
        self._execute_query(query)

    def add_category(self, category: Category) -> None:
        query = categories_queries.insert_into_categories(category)
        self._execute_query(query)

    def add_transaction(self, transaction: Transaction) -> None:
        query = transactions_queries.insert_into_transactions(transaction)
        self._execute_query(query)

    def get_all_transactions(self) -> List[Transaction]:
        query = transactions_queries.get_all_transactions
        transactions_data = self._execute_query(query)
        return [
            extract_transaction(transaction_data)
            for transaction_data in transactions_data
        ]

    def delete_transaction(self, transaction_id: int) -> None:
        query = transactions_queries.delete_transaction_by_id(transaction_id)
        self._execute_query(query)

    def get_breakdown_by_categories(self) -> Dict[str, float]:
        query = transactions_queries.get_amount_by_category
        data = self._execute_query(query)
        categories_total = dict()
        for item in data:
            category_name = item.get(c.CATEGORY, "")
            total_amount = float(item.get(c.TOTAL_AMOUNT, 0))
            categories_total[category_name] = total_amount
        return categories_total


if __name__ == "__main__":
    db = MySqlManager("bank")
    print(db.get_breakdown_by_categories())
