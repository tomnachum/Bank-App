import React from "react";
import "./Transaction.css";
import ListGroup from "react-bootstrap/ListGroup";
import Badge from "react-bootstrap/Badge";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faTrash } from "@fortawesome/free-solid-svg-icons";
import Button from "react-bootstrap/Button";

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
        <div className="ms-2">{props.transaction.vendor}</div>
        <div className="ms-2 center-vertically">
          <div>{getDate()}</div>
          {getTime()}
        </div>
        <Badge
          bg={props.transaction.amount > 0 ? "success" : "danger"}
          pill
          className="center-vertically amount"
        >
          {props.transaction.amount}
        </Badge>
        <Button
          onClick={() => {
            props.delete(props.transaction.id);
          }}
          variant="outline-dark"
          className="delete-btn"
        >
          <FontAwesomeIcon icon={faTrash} />
        </Button>
      </div>
    </ListGroup.Item>
  );
}
