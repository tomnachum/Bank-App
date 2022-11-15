import json
import utils.constants as c
from my_sql_manager import MySqlManager
from utils.connection import get_connection_to_db, get_general_connection
from queries.general_queries import create_db as q_create_db, delete_db
from queries.categories_queries import create_categories_table
from queries.transactions_queries import create_transactions_table
from queries.users_queries import create_users_table
from objects.raw_data_to_object import (
    extract_category,
    extract_transaction,
    extract_user,
)


def create_db():
    try:
        connection = get_general_connection()
        with connection.cursor() as cursor:
            # in case db already exist, delete it first
            cursor.execute(delete_db)
            cursor.execute(q_create_db)
            print("db created successfully")
            connection.commit()
    except Exception as e:
        print(e)


def create_tables():
    try:
        connection = get_connection_to_db(c.DB_NAME)
        with connection.cursor() as cursor:
            cursor.execute(create_categories_table)
            print("categories table created successfully")
            cursor.execute(create_users_table)
            print("users table created successfully")
            cursor.execute(create_transactions_table)
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
        user = extract_user(user_data)
        db.add_user(user)
    print("initialized users table successfully")


def init_categories_table(db, categories_data):
    for category_data in categories_data:
        category = extract_category(category_data)
        db.add_category(category)
    print("initialized categories table successfully")


def init_transactions_table(db, transactions_data):
    for transaction_data in transactions_data:
        transaction = extract_transaction(transaction_data)
        db.add_transaction(transaction)
    print("initialized transactions table successfully")


def init_tables():
    db = MySqlManager(c.DB_NAME)
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
