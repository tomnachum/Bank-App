from db.utils.constants import DB_NAME

delete_db = f"""
            DROP DATABASE IF EXISTS {DB_NAME};
            """


create_db = f"""
            CREATE DATABASE IF NOT EXISTS {DB_NAME};
            """
