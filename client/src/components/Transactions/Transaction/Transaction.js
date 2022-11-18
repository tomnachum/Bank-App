import React from "react";
import "./Transaction.css";
import ListGroup from "react-bootstrap/ListGroup";
import Badge from "react-bootstrap/Badge";

export default function Transaction(props) {
  function getDate() {
    const date = props.transaction.date.split(" ")[0];
    const [year, month, day] = date.split("-");
    return `${day}/${month}/${year}`;
  }

  function getHour() {
    const time = props.transaction.date.split(" ")[1];
    return time.slice(0, -3);
  }

  return (
    <ListGroup.Item
      as="li"
      className="d-flex justify-content-between align-items-start"
    >
      <div className="container">
        <div className="ms-2">
          <div className="fw-bold">{props.transaction.category}</div>
          {props.transaction.vendor}
        </div>
        <div className="ms-2 center-vertically">
          <div>{getDate()}</div>
          {getHour()}
        </div>
        <Badge
          bg={props.transaction.amount > 0 ? "success" : "danger"}
          pill
          className="center-vertically amount"
        >
          {Math.abs(props.transaction.amount)}
        </Badge>
      </div>
    </ListGroup.Item>
  );
}
