import React from "react";
import "./Transactions.css";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import Badge from "react-bootstrap/Badge";

export default function Transactions() {
  return (
    <Card style={{ width: "35rem" }}>
      <Card.Header as="h3">Transactions</Card.Header>
      <ListGroup as="ol">
        <ListGroup.Item
          as="li"
          className="d-flex justify-content-between align-items-start"
        >
          <div className="ms-2 me-auto">
            <div className="fw-bold">Category</div>
            vendor
          </div>
          <div className="ms-2 me-auto center-vertically">date</div>
          <Badge bg="success" pill className="center-vertically amount">
            positive amount
          </Badge>
        </ListGroup.Item>
      </ListGroup>
    </Card>
  );
}
