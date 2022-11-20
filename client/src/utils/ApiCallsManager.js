import axios from "axios";
import * as c from "./Constants";

export default class ApiCallsManager {
  static async getBalance() {
    const res = await axios.get(
      `${c.SERVER_DOMAIN}${c.USERS}/${c.USER_ID}/${c.BALANCE}`
    );
    const balance = res.data.balance;
    return balance;
  }

  static async getBreakdown() {
    const res = await axios.get(c.SERVER_DOMAIN + c.BREAKDOWN);
    const breakdown = res.data.breakdown;
    return breakdown;
  }

  static async getCategories() {
    const res = await axios.get(c.SERVER_DOMAIN + c.CATEGORIES);
    const categories = res.data.categories;
    return categories;
  }

  static addTransaction(transaction) {
    return axios.post(c.SERVER_DOMAIN + c.TRANSACTIONS, transaction);
  }

  static async getTransactions() {
    const res = await axios.get(c.SERVER_DOMAIN + c.TRANSACTIONS);
    const transactions = res.data.transactions;
    return transactions;
  }

  static deleteTransaction(id) {
    return axios.delete(c.SERVER_DOMAIN + c.TRANSACTIONS + `/${id}`);
  }
}
