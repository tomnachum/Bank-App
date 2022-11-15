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


get_all_transactions = f"""
    SELECT *
    FROM {c.TRANSACTIONS_TABLE_NAME}
"""


def delete_transaction_by_id(transaction_id):
    return f"""
        DELETE
        FROM {c.TRANSACTIONS_TABLE_NAME}
        WHERE id={transaction_id}
    """


get_amount_by_category = f"""
    SELECT c.name as category, CAST(SUM(t.amount) as DECIMAL(10,2)) as total
    FROM {c.TRANSACTIONS_TABLE_NAME} AS t JOIN {c.CATEGORIES_TABLE_NAME} AS c
    ON c.id = t.categoryId
    GROUP BY t.categoryId
"""
