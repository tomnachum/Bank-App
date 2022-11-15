from objects.user import User
from objects.category import Category
from objects.transaction import Transaction
from utils.connection import get_connection_to_db
from queries.categories_queries import *
from queries.transactions_queries import *
from queries.users_queries import *


class mySQLManager:
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

    def add_user(self, user: User):
        query = insert_into_users(user)
        self._execute_query(query)

    def add_category(self, category: Category):
        query = insert_into_categories(category)
        self._execute_query(query)

    def add_transaction(self, transaction: Transaction):
        query = insert_into_transactions(transaction)
        self._execute_query(query)
