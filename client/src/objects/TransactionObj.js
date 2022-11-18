export default class TransactionObj {
  constructor(amount, vendor, date, categoryId) {
    this.amount = amount;
    this.vendor = vendor;
    this.date = date;
    this.categoryId = categoryId;
  }
}
