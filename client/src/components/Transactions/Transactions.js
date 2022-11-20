import React, { useEffect, useState } from "react";
import "./Transactions.css";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import Transaction from "./Transaction/Transaction";
import transactionsComparator from "../../utils/TransactionsComparator";
import TransactionObj from "../../objects/TransactionObj";
import parseDate from "../../utils/ParseDate";
import axios from "axios";
import * as c from "../../utils/Constants";
import Notification from "../../ui-components/Notification/Notification";

export default function Transactions(props) {
  const [transactions, setTransactions] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);

  async function fetchTransactions() {
    const res = await axios.get(c.SERVER_DOMAIN + c.TRANSACTIONS);
    const transactionsData = res.data.transactions;
    const transactionsObj = transactionsData.map(
      t =>
        new TransactionObj(
          t.id,
          t.amount,
          t.vendor,
          parseDate(t.date),
          t.categoryId
        )
    );
    setTransactions(transactionsObj);
  }

  useEffect(() => {
    fetchTransactions();
  }, []);

  async function deleteTransaction(id) {
    setIsModalOpen(true);
    await axios.delete(c.SERVER_DOMAIN + c.TRANSACTIONS + `/${id}`);
    await fetchTransactions();
    props.updateBalance();
  }

  return (
    <>
      <Card style={{ width: "35rem" }}>
        <Card.Header as="h3">Transactions</Card.Header>
        <ListGroup as="ol">
          {transactions.sort(transactionsComparator).map((t, i) => (
            <Transaction
              key={i}
              transaction={t}
              delete={deleteTransaction}
            ></Transaction>
          ))}
        </ListGroup>
      </Card>
      <Notification
        show={isModalOpen}
        setIsOpen={setIsModalOpen}
        msg="Transaction deleted successfully."
      ></Notification>
    </>
  );
}
