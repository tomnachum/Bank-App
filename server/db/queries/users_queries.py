from db.utils.constants import USERS_TABLE_NAME
from db.objects import User

create_users_table = f"""
            CREATE TABLE IF NOT EXISTS {USERS_TABLE_NAME}(
                id INT NOT NULL PRIMARY KEY,
                name VARCHAR(255),
                balance FLOAT,
                UNIQUE (name)
                );
            """


def insert_into_users(user: User):
    return f"""
            INSERT IGNORE INTO {USERS_TABLE_NAME} VALUES
            ({user.id}, '{user.name}', {user.balance})
    """


def get_user_by_id(user_id: int):
    return f"""
        SELECT *
        FROM {USERS_TABLE_NAME}
        WHERE id={user_id}
    """


def update_balance(user_id: int, to_add: float):
    return f"""
        UPDATE {USERS_TABLE_NAME}
        SET balance = balance + {to_add}
        WHERE id={user_id}
    """


def get_balance(user_id: int):
    return f"""
        SELECT balance
        FROM {USERS_TABLE_NAME}
        WHERE id={user_id}
    """
