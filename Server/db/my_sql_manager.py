from typing import List, Dict
from db.db_manager import DataBaseManager
from db.objects import User, Category, Transaction, extract_transaction
from db.queries import *
from db.utils import get_connection_to_db, CATEGORY, TOTAL_AMOUNT


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
        query = insert_into_users(user)
        self._execute_query(query)

    def add_category(self, category: Category) -> None:
        query = insert_into_categories(category)
        self._execute_query(query)

    def add_transaction(self, transaction: Transaction) -> None:
        print("in add")
        print(transaction.amount)
        query = insert_into_transactions(transaction)
        self._execute_query(query)
        print("finished add")

    def get_all_transactions(self) -> List[Transaction]:
        query = get_all_transactions
        transactions_data = self._execute_query(query)
        return [
            extract_transaction(transaction_data)
            for transaction_data in transactions_data
        ]

    def delete_transaction(self, transaction_id: int) -> None:
        query = delete_transaction_by_id(transaction_id)
        self._execute_query(query)

    def get_breakdown_by_categories(self) -> Dict[str, float]:
        query = get_amount_by_category
        data = self._execute_query(query)
        categories_total = dict()
        for item in data:
            category_name = item.get(CATEGORY, "")
            total_amount = float(item.get(TOTAL_AMOUNT, 0))
            categories_total[category_name] = total_amount
        return categories_total
