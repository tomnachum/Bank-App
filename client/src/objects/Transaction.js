export default class Transaction {
  constructor(amount, vendor, date, category) {
    this.amount = amount;
    this.vendor = vendor;
    this.date = date;
    this.category = category;
  }
}
