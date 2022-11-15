import utils.constants as c

delete_db = f"""
            DROP DATABASE IF EXISTS {c.DB_NAME};
            """


create_db = f"""
            CREATE DATABASE IF NOT EXISTS {c.DB_NAME};
            """
