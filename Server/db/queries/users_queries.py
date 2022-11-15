import utils.constants as c
from objects.user import User

create_users_table = f"""
            CREATE TABLE IF NOT EXISTS users(
                id INT NOT NULL PRIMARY KEY,
                name VARCHAR(255),
                balance FLOAT,
                UNIQUE (name)
                );
            """


def insert_into_users(user: User):
    return f"""
            INSERT IGNORE INTO {c.USERS_TABLE_NAME} VALUES
            ({user.id}, '{user.name}', {user.balance})
    """
