import React from "react";
import "./Balance.css";
import Card from "react-bootstrap/Card";

export default function Balance(props) {
  return (
    <Card bg="light">
      <Card.Body className="balance">
        <strong>Balance: </strong>
        <span className={props.balance >= 0 ? "plus" : "minus"}>
          {props.balance}
        </span>
      </Card.Body>
    </Card>
  );
}
