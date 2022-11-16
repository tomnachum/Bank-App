from db.utils.constants import CATEGORIES_TABLE_NAME
from db.objects import Category

create_categories_table = f"""
            CREATE TABLE IF NOT EXISTS {CATEGORIES_TABLE_NAME}(
                id INT NOT NULL PRIMARY KEY,
                name VARCHAR(255),
                UNIQUE (name)
                );
            """


def insert_into_categories(category: Category):
    return f"""
            INSERT IGNORE INTO {CATEGORIES_TABLE_NAME} VALUES
            ({category.id}, '{category.name}')
    """


def get_category_by_id(category_id: int):
    return f"""
        SELECT *
        FROM {CATEGORIES_TABLE_NAME}
        WHERE id={category_id}
    """


get_all_categories = f"""
    SELECT * 
    FROM {CATEGORIES_TABLE_NAME}
    """
