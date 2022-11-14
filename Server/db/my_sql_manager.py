import pymysql
import queries as q


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

    def _execute_select_query(self, query):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except Exception as e:
            print(e)

    def _execute_query(self, query):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                self.connection.commit()
        except Exception as e:
            print(e)

    def add_user(self, id, name, balance):
        query = q.insert_into_users(id, name, balance)
        self._execute_query(query)

    def add_category(self, id, name):
        query = q.insert_into_categories(id, name)
        self._execute_query(query)

    def add_transaction(self, id, amount, vendor, categoryId, userId):
        query = q.insert_into_transactions(id, amount, vendor, categoryId, userId)
        self._execute_query(query)
