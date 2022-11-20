export default class TransactionObj {
  constructor(id, amount, vendor, date, categoryId, userId) {
    this.id = id;
    this.amount = amount;
    this.vendor = vendor;
    this.date = date;
    this.categoryId = categoryId;
    this.userId = userId;
  }
}
