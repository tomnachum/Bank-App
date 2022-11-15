import pymysql
import queries as q
from objects.user import User
from objects.category import Category
from objects.transaction import Transaction
import utils.constants as c


class mySQLManager:
    def __init__(self, db_name) -> None:
        """
        This class assumes that the DB is already created.
        """
        self.connection = pymysql.connect(
            host=c.CONNECTION_HOST,
            user=c.CONNECTION_USER,
            password=c.CONNECTION_PASSWORD,
            db=db_name,
            charset=c.CONNECTION_CHARSET,
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
