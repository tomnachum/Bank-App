import React, { useEffect, useState } from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import * as c from "../../../utils/Constants";
import "./InsertTransaction.css";
import Notification from "../../../ui-components/Notification/Notification";
import ApiCallsManager from "../../../utils/ApiCallsManager";
import TransactionObj from "../../../objects/TransactionObj";

export default function InsertTransaction(props) {
  const [categories, setCategories] = useState([]);
  const [transactionInput, setTransactionInput] = useState({
    amount: "",
    vendor: "",
    categoryId: "",
  });
  const [validated, setValidated] = useState(false);
  const [isModalOpen, setIsModalOpen] = useState(false);

  useEffect(() => {
    async function fetchCategories() {
      const categoriesData = await ApiCallsManager.getCategories();
      setCategories(categoriesData);
    }
    fetchCategories();
  }, []);

  function handleInput(e) {
    setTransactionInput({
      ...transactionInput,
      [e.target.name]: e.target.value,
    });
  }

  async function handleSubmit(e) {
    const form = e.currentTarget;
    e.preventDefault();
    e.stopPropagation();
    if (form.checkValidity() === true) {
      setIsModalOpen(true);
      let sign = e.nativeEvent.submitter.name === "Deposit" ? 1 : -1;
      await ApiCallsManager.addTransaction(
        new TransactionObj(
          null,
          sign * +transactionInput.amount,
          transactionInput.vendor,
          null,
          transactionInput.categoryId,
          c.USER_ID
        )
      );
      props.updateBalance();
      setTransactionInput({
        amount: "",
        vendor: "",
        categoryId: "",
      });
      setValidated(false);
    } else {
      setValidated(true);
    }
  }

  return (
    <div>
      <Card style={{ width: "25rem", margin: "auto" }}>
        <Card.Header as="h3">Insert Transaction</Card.Header>
        <Card.Body>
          <Form
            noValidate
            validated={validated}
            onSubmit={handleSubmit}
            autoComplete="off"
          >
            <Form.Group className="mb-3" controlId="formBasicEmail">
              <Form.Label>Amount</Form.Label>
              <Form.Control
                min="0.01"
                max="100000"
                type="number"
                step="0.01"
                placeholder="Enter amount"
                name="amount"
                value={transactionInput.amount}
                onChange={handleInput}
                required
              />
              <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
              <Form.Control.Feedback type="invalid">
                Please choose amount between 0 and 100,000.
              </Form.Control.Feedback>
            </Form.Group>

            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Vendor</Form.Label>
              <Form.Control
                type="text"
                placeholder="Enter vendor"
                maxLength={20}
                value={transactionInput.vendor}
                onChange={handleInput}
                name="vendor"
                required
              />
              <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
              <Form.Control.Feedback type="invalid">
                Please choose vendor.
              </Form.Control.Feedback>
            </Form.Group>

            <Form.Group className="mb-3">
              <Form.Label>Category</Form.Label>
              <Form.Select
                value={transactionInput.categoryId}
                onChange={handleInput}
                name="categoryId"
                required
              >
                <option value="" hidden>
                  Select category
                </option>
                {categories.sort().map((c, i) => (
                  <option key={i} value={c.id}>
                    {c.name}
                  </option>
                ))}
              </Form.Select>
              <Form.Control.Feedback>Looks good!</Form.Control.Feedback>
              <Form.Control.Feedback type="invalid">
                Please select category.
              </Form.Control.Feedback>
            </Form.Group>

            <Button variant="success" name="Deposit" type="submit">
              Deposit
            </Button>
            <Button
              name="Withdraw"
              variant="danger"
              style={{ float: "right" }}
              type="submit"
            >
              Withdraw
            </Button>
          </Form>
        </Card.Body>
      </Card>
      <Notification
        show={isModalOpen}
        setIsOpen={setIsModalOpen}
        msg="Transaction added successfully."
      ></Notification>
    </div>
  );
}
