import React from "react";
import "./Transaction.css";
import ListGroup from "react-bootstrap/ListGroup";
import Badge from "react-bootstrap/Badge";

export default function Transaction(props) {
  function getDate() {
    const date = props.transaction.date;
    const year = date.getFullYear();
    const month = date.getMonth();
    const day = date.getDate();
    return `${day}/${month}/${year}`;
  }

  function getTime() {
    const date = props.transaction.date;
    const hours = date.getHours();
    const minutes = date.getMinutes();
    return `${hours}:${minutes < 10 ? "0" : ""}${minutes}`;
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
          {getTime()}
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
