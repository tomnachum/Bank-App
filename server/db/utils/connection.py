import pymysql
from db.utils import constants as c


def get_general_connection():
    return pymysql.connect(
        host=c.CONNECTION_HOST, user=c.CONNECTION_USER, password=c.CONNECTION_PASSWORD
    )


def get_connection_to_db(db_name: str):
    return pymysql.connect(
        host=c.CONNECTION_HOST,
        user=c.CONNECTION_USER,
        password=c.CONNECTION_PASSWORD,
        db=db_name,
        charset=c.CONNECTION_CHARSET,
        cursorclass=pymysql.cursors.DictCursor,
    )
