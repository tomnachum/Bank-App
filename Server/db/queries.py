import utils.constants as c


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
                balance INT,
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
                amount INT,
                vendor VARCHAR(255),
                categoryId INT,
                userId INT,
                FOREIGN KEY(categoryId) REFERENCES {c.CATEGORIES_TABLE_NAME}(id),
                FOREIGN KEY(userId) REFERENCES {c.USERS_TABLE_NAME}(id)
                );
            """


def insert_into_users(id, name, balance):
    return f"""
            INSERT IGNORE INTO {c.USERS_TABLE_NAME} VALUES
            ({id}, '{name}', {balance})
    """


def insert_into_categories(id, name):
    return f"""
            INSERT IGNORE INTO {c.CATEGORIES_TABLE_NAME} VALUES
            ({id}, '{name}')
    """


def insert_into_transactions(id, amount, vendor, categoryId, userId):
    return f"""
            INSERT IGNORE INTO {c.TRANSACTIONS_TABLE_NAME} VALUES
            ({id}, {amount}, '{vendor}', {categoryId}, {userId})
    """
