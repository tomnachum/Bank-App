import React, { useEffect, useState } from "react";
import Card from "react-bootstrap/Card";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import * as c from "../../../utils/Constants";
import axios from "axios";

export default function InsertTransaction() {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    async function fetchCategories() {
      const res = await axios.get(c.SERVER_DOMAIN + c.CATEGORIES);
      const categoriesData = res.data.categories;
      const categories = categoriesData.map(c => c.name);
      setCategories(categories);
    }
    fetchCategories();
  }, []);

  return (
    <div>
      <Card style={{ width: "25rem" }}>
        <Card.Header as="h3">Insert Transaction</Card.Header>
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
                {categories.sort().map((c, i) => (
                  <option key={i} value={c}>
                    {c}
                  </option>
                ))}
              </Form.Select>
            </Form.Group>

            <Button variant="primary" type="submit">
              Submit
            </Button>
          </Form>
        </Card.Body>
      </Card>
    </div>
  );
}
