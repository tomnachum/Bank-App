import React from "react";
import "./Operations.css";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";

export default function Operations() {
  return (
    <Card style={{ width: "18rem" }}>
      <Card.Header as="h6">Insert Transaction</Card.Header>
      <Card.Body>
        <Form>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Amount</Form.Label>
            <div className="side-by-side">
              <Form.Select>
                <option>Outcome</option>
                <option>Income</option>
              </Form.Select>
              <Form.Control
                min="0.01"
                max="100000"
                type="number"
                step="0.01"
                placeholder="Enter amount"
              />
            </div>
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Vendor</Form.Label>
            <Form.Control
              type="text"
              placeholder="Enter vendor"
              maxLength={20}
            />
          </Form.Group>

          <Form.Group className="mb-3">
            <Form.Label>Category</Form.Label>
            <Form.Select>
              <option value="" selected disabled hidden>
                Select category
              </option>
              <option>1</option>
              <option>2</option>
              <option>3</option>
              <option>4</option>
            </Form.Select>
          </Form.Group>

          <Button variant="primary" type="submit">
            Submit
          </Button>
        </Form>
      </Card.Body>
    </Card>
  );
}
