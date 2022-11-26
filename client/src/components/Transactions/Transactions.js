import React, { useEffect, useState } from "react";
import "./Transactions.css";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import Transaction from "./Transaction/Transaction";
import transactionsComparator from "../../utils/TransactionsComparator";
import TransactionObj from "../../objects/TransactionObj";
import parseDate from "../../utils/ParseDate";
import * as c from "../../utils/Constants";
import Notification from "../../ui-components/Notification/Notification";
import ApiCallsManager from "../../utils/ApiCallsManager";

export default function Transactions(props) {
  const [transactions, setTransactions] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);

  async function fetchTransactions() {
    const transactionsData = await ApiCallsManager.getTransactions();
    const transactionsObj = transactionsData.map(
      t =>
        new TransactionObj(
          t.id,
          t.amount,
          t.vendor,
          parseDate(t.date),
          t.categoryId,
          c.USER_ID
        )
    );
    setTransactions(transactionsObj);
  }

  useEffect(() => {
    fetchTransactions();
  }, []);

  async function deleteTransaction(id) {
    setIsModalOpen(true);
    await ApiCallsManager.deleteTransaction(id);
    await fetchTransactions();
    props.updateBalance();
  }

  return (
    <>
      <ListGroup as="ol" style={{ width: "50rem", margin: "auto" }}>
        {transactions.sort(transactionsComparator).map((t, i) => (
          <Transaction
            key={i}
            transaction={t}
            delete={deleteTransaction}
          ></Transaction>
        ))}
      </ListGroup>
      <Notification
        show={isModalOpen}
        setIsOpen={setIsModalOpen}
        msg="Transaction deleted successfully."
      ></Notification>
    </>
  );
}
