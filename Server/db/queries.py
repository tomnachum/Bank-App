import utils.constants as c
from objects.user import User
from objects.category import Category
from objects.transaction import Transaction


delete_db = f"""
            DROP DATABASE IF EXISTS {c.DB_NAME};
            """


create_db = f"""
            CREATE DATABASE IF NOT EXISTS {c.DB_NAME};
            """


create_users_table = f"""
            CREATE TABLE IF NOT EXISTS users(
                id INT NOT NULL,
                name VARCHAR(255),
                balance FLOAT,
                PRIMARY KEY(id, name)
                );
            """


create_categories_table = f"""
            CREATE TABLE IF NOT EXISTS {c.CATEGORIES_TABLE_NAME}(
                id INT NOT NULL,
                name VARCHAR(255),
                PRIMARY KEY(id, name)
                );
            """

create_transactions_table = f"""
            CREATE TABLE IF NOT EXISTS {c.TRANSACTIONS_TABLE_NAME}(
                id INT NOT NULL PRIMARY KEY,
                amount FLOAT,
                vendor VARCHAR(255),
                date VARCHAR(255),
                categoryId INT,
                userId INT,
                FOREIGN KEY(categoryId) REFERENCES {c.CATEGORIES_TABLE_NAME}(id),
                FOREIGN KEY(userId) REFERENCES {c.USERS_TABLE_NAME}(id)
                );
            """


def insert_into_users(user: User):
    return f"""
            INSERT IGNORE INTO {c.USERS_TABLE_NAME} VALUES
            ({user.id}, '{user.name}', {user.balance})
    """


def insert_into_categories(category: Category):
    return f"""
            INSERT IGNORE INTO {c.CATEGORIES_TABLE_NAME} VALUES
            ({category.id}, '{category.name}')
    """


def insert_into_transactions(transaction: Transaction):
    return f"""
            INSERT IGNORE INTO {c.TRANSACTIONS_TABLE_NAME} VALUES
            ({transaction.id}, {transaction.amount}, '{transaction.vendor}', '{transaction.date}', {transaction.categoryId}, {transaction.userId})
    """
