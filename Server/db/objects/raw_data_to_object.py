import utils.constants as c
from objects.category import Category
from objects.transaction import Transaction
from objects.user import User


def extract_transaction(transaction_data):
    amount = transaction_data.get(c.TRANSACTION_AMOUNT, 0)
    vendor = transaction_data.get(c.TRANSACTION_VENDOR, None)
    date = transaction_data.get(c.TRANSACTION_DATE, None)
    categoryId = transaction_data.get(c.TRANSACTION_CATEGORY_ID, 0)
    userId = transaction_data.get(c.TRANSACTION_USER_ID, 0)
    transaction = Transaction(amount, vendor, categoryId, userId, date)
    return transaction


def extract_user(user_data):
    name = user_data.get(c.USER_NAME, None)
    balance = user_data.get(c.USER_BALANCE, 0)
    user = User(name, balance)
    return user


def extract_category(category_data):
    name = category_data.get(c.CATEGORY_NAME, None)
    category = Category(name)
    return category
