import pymysql
import queries as q
from objects.user import User
from objects.category import Category
from objects.transaction import Transaction


class mySQLManager:
    def __init__(self, db_name) -> None:
        """
        This class assumes that the DB is already created.
        """
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db=db_name,
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor,
        )
        self.connection.autocommit(True)

    def _execute_select_query(self, query):
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)

    def _execute_query(self, query):
        try:
            self.connection.ping()
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            print(e)

    def add_user(self, user: User):
        query = q.insert_into_users(user)
        self._execute_query(query)

    def add_category(self, category: Category):
        query = q.insert_into_categories(category)
        self._execute_query(query)

    def add_transaction(self, transaction: Transaction):
        query = q.insert_into_transactions(transaction)
        self._execute_query(query)
