import utils.constants as c
from objects.transaction import Transaction

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


def insert_into_transactions(transaction: Transaction):
    return f"""
            INSERT IGNORE INTO {c.TRANSACTIONS_TABLE_NAME} VALUES
            ({transaction.id}, {transaction.amount}, '{transaction.vendor}', '{transaction.date}', {transaction.categoryId}, {transaction.userId})
    """
