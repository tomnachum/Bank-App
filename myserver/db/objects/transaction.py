from datetime import datetime


class Transaction:
    id = 0

    def __init__(
        self,
        amount: float,
        vendor: str,
        categoryId: int,
        userId: int,
        date: str = None,
        id: int = None,
    ) -> None:
        self.id = id if id is not None else Transaction.id
        self.amount = amount
        self.vendor = vendor
        self.categoryId = categoryId
        self.userId = userId
        self.date = date if date else self._getCurrentTime()
        Transaction.id += 1

    def _getCurrentTime(self):
        currentTime = datetime.now().strftime("%m/%d/%Y %I:%M %p")
        return datetime.strptime(currentTime, "%m/%d/%Y %I:%M %p")
