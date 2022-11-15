import pymysql
import queries as q
import utils.constants as c
import json
from my_sql_manager import mySQLManager
from objects.user import User
from objects.category import Category
from objects.transaction import Transaction


def create_db():
    connection = pymysql.connect(host="localhost", user="root", password="")
    try:
        with connection.cursor() as cursor:
            # in case db already exist, delete it first
            cursor.execute(q.delete_db)
            cursor.execute(q.create_db)
            print("db created successfully")
            connection.commit()
    except Exception as e:
        print(e)


def create_tables():
    connection = pymysql.connect(
        host=c.CONNECTION_HOST,
        user=c.CONNECTION_USER,
        password=c.CONNECTION_PASSWORD,
        db=c.DB_NAME,
        charset=c.CONNECTION_CHARSET,
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute(q.create_categories_table)
            print("categories table created successfully")
            cursor.execute(q.create_users_table)
            print("users table created successfully")
            cursor.execute(q.create_transactions_table)
            print("transactions table created successfully")
            connection.commit()
    except Exception as e:
        print(e)


def get_data_from_json():
    data_file = open(c.DATA_DIR)
    data = json.load(data_file)
    data_file.close()
    return data


def init_users_table(db, users_data):
    for user_data in users_data:
        id = user_data.get(c.USER_ID, 0)
        name = user_data.get(c.USER_NAME, None)
        balance = user_data.get(c.USER_BALANCE, 0)
        user = User(id, name, balance)
        db.add_user(user)
    print("initialized users table successfully")


def init_categories_table(db, categories_data):
    for category_data in categories_data:
        id = category_data.get(c.CATEGORY_ID, 0)
        name = category_data.get(c.CATEGORY_NAME, None)
        category = Category(id, name)
        db.add_category(category)
    print("initialized categories table successfully")


def init_transactions_table(db, transactions_data):
    for transaction_data in transactions_data:
        id = transaction_data.get(c.TRANSACTION_ID, 0)
        amount = transaction_data.get(c.TRANSACTION_AMOUNT, 0)
        vendor = transaction_data.get(c.TRANSACTION_VENDOR, None)
        date = transaction_data.get(c.TRANSACTION_DATE, None)
        categoryId = transaction_data.get(c.TRANSACTION_CATEGORY_ID, 0)
        userId = transaction_data.get(c.TRANSACTION_USER_ID, 0)
        transaction = Transaction(id, amount, vendor, categoryId, userId, date)
        db.add_transaction(transaction)
    print("initialized transactions table successfully")


def init_tables():
    db = mySQLManager(c.DB_NAME)
    data = get_data_from_json()
    users_data = data.get(c.USERS_TABLE_NAME, [])
    init_users_table(db, users_data)
    categories_data = data.get(c.CATEGORIES_TABLE_NAME, [])
    init_categories_table(db, categories_data)
    transactions_data = data.get(c.TRANSACTIONS_TABLE_NAME, [])
    init_transactions_table(db, transactions_data)


if __name__ == "__main__":
    print("########## Creating DB")
    create_db()
    print()
    print("########## Creating Tables")
    create_tables()
    print()
    print("########## Initializing Tables")
    init_tables()
