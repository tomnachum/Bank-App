import React, { useEffect, useState } from "react";
import "./Breakdown.css";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import * as c from "../../utils/Constants";
import axios from "axios";

export default function Breakdown() {
  const [breakdown, setBreakdown] = useState([]);

  useEffect(() => {
    async function fetchBreakdown() {
      const res = await axios.get(c.SERVER_DOMAIN + c.BREAKDOWN);
      const breakdownData = res.data.breakdown;
      setBreakdown(breakdownData);
    }
    fetchBreakdown();
  }, []);

  return (
    <Card style={{ width: "18rem" }}>
      <Card.Header as="h3">Breakdown</Card.Header>
      <ListGroup variant="flush">
        {breakdown.map((b, i) => (
          <ListGroup.Item key={i}>
            <span>{b.category}: </span>
            <span className="total">{b.total}</span>
          </ListGroup.Item>
        ))}
      </ListGroup>
    </Card>
  );
}
