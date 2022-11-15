import pymysql
import queries as q
from utils.constants import DB_NAME, DATA_DIR
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
        host="localhost",
        user="root",
        password="",
        db=DB_NAME,
        charset="utf8",
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
    data_file = open(DATA_DIR)
    data = json.load(data_file)
    data_file.close()
    return data


def init_users_table(db, users_data):
    for user_data in users_data:
        id = user_data.get("id", 0)
        name = user_data.get("name", None)
        balance = user_data.get("balance", 0)
        user = User(id, name, balance)
        db.add_user(user)
    print("initialized users table successfully")


def init_categories_table(db, categories_data):
    for category_data in categories_data:
        id = category_data.get("id", 0)
        name = category_data.get("name", None)
        category = Category(id, name)
        db.add_category(category)
    print("initialized categories table successfully")


def init_transactions_table(db, transactions_data):
    for transaction_data in transactions_data:
        id = transaction_data.get("id", 0)
        amount = transaction_data.get("amount", 0)
        vendor = transaction_data.get("vendor", None)
        date = transaction_data.get("date", None)
        categoryId = transaction_data.get("categoryId", 0)
        userId = transaction_data.get("userId", 0)
        transaction = Transaction(id, amount, vendor, categoryId, userId, date)
        db.add_transaction(transaction)
    print("initialized transactions table successfully")


def init_tables():
    db = mySQLManager(DB_NAME)
    data = get_data_from_json()
    users_data = data.get("users", [])
    init_users_table(db, users_data)
    categories_data = data.get("categories", [])
    init_categories_table(db, categories_data)
    transactions_data = data.get("transactions", [])
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
