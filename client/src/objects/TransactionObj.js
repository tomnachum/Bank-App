export default class TransactionObj {
  constructor(id, amount, vendor, date, categoryId) {
    this.id = id;
    this.amount = amount;
    this.vendor = vendor;
    this.date = date;
    this.categoryId = categoryId;
  }
}
