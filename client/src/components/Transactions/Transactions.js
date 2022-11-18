import React from "react";
import "./Transactions.css";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import Transaction from "./Transaction/Transaction";

export default function Transactions(props) {
  return (
    <Card style={{ width: "35rem" }}>
      <Card.Header as="h3">Transactions</Card.Header>
      <ListGroup as="ol">
        {props.transactions.map(t => (
          <Transaction transaction={t}></Transaction>
        ))}
      </ListGroup>
    </Card>
  );
}
