import pymysql
import queries as q
from utils.constants import DB_NAME, DATA_DIR
import json
from my_sql_manager import mySQLManager


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


def init_users_table(db, users):
    for user in users:
        id = user.get("id", 0)
        name = user.get("name", None)
        balance = user.get("balance", 0)
        db.add_user(id, name, balance)
    print("initialized users table successfully")


def init_categories_table(db, categories):
    for category in categories:
        id = category.get("id", 0)
        name = category.get("name", None)
        db.add_category(id, name)
    print("initialized categories table successfully")


def init_transactions_table(db, transactions):
    for transaction in transactions:
        id = transaction.get("id", 0)
        amount = transaction.get("amount", 0)
        vendor = transaction.get("vendor", None)
        categoryId = transaction.get("categoryId", 0)
        userId = transaction.get("userId", 0)
        db.add_transaction(id, amount, vendor, categoryId, userId)
    print("initialized transactions table successfully")


def init_tables():
    db = mySQLManager(DB_NAME)
    data = get_data_from_json()
    users = data.get("users", [])
    init_users_table(db, users)
    categories = data.get("categories", [])
    init_categories_table(db, categories)
    transactions = data.get("transactions", [])
    init_transactions_table(db, transactions)


if __name__ == "__main__":
    print("########## Creating DB")
    create_db()
    print()
    print("########## Creating Tables")
    create_tables()
    print()
    print("########## Initializing Tables")
    init_tables()
