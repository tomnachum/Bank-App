import utils.constants as c
from objects.category import Category

create_categories_table = f"""
            CREATE TABLE IF NOT EXISTS {c.CATEGORIES_TABLE_NAME}(
                id INT NOT NULL PRIMARY KEY,
                name VARCHAR(255),
                UNIQUE (name)
                );
            """


def insert_into_categories(category: Category):
    return f"""
            INSERT IGNORE INTO {c.CATEGORIES_TABLE_NAME} VALUES
            ({category.id}, '{category.name}')
    """
