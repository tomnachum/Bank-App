from db.objects import Transaction, Category, User
from db.utils import constants as c


def extract_transaction(transaction_data):
    id = transaction_data.get(c.TRANSACTION_ID, None)
    amount = transaction_data.get(c.TRANSACTION_AMOUNT, 0)
    vendor = transaction_data.get(c.TRANSACTION_VENDOR, None)
    date = transaction_data.get(c.TRANSACTION_DATE, None)
    categoryId = transaction_data.get(c.TRANSACTION_CATEGORY_ID, 0)
    userId = transaction_data.get(c.TRANSACTION_USER_ID, 0)
    transaction = Transaction(amount, vendor, categoryId, userId, date, id)
    return transaction


def extract_user(user_data):
    id = user_data.get(c.USER_ID, None)
    name = user_data.get(c.USER_NAME, None)
    balance = user_data.get(c.USER_BALANCE, 0)
    user = User(name, balance, id)
    return user


def extract_category(category_data):
    id = category_data.get(c.CATEGORY_ID, None)
    name = category_data.get(c.CATEGORY_NAME, None)
    category = Category(name, id)
    return category
