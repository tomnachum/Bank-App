import React, { useEffect, useState } from "react";
import "./Breakdown.css";
import Card from "react-bootstrap/Card";
import ListGroup from "react-bootstrap/ListGroup";
import ApiCallsManager from "../../utils/ApiCallsManager";

export default function Breakdown() {
  const [breakdown, setBreakdown] = useState([]);

  useEffect(() => {
    async function fetchBreakdown() {
      const breakdownData = await ApiCallsManager.getBreakdown();
      setBreakdown(breakdownData);
    }
    fetchBreakdown();
  }, []);

  return (
    <ListGroup style={{ width: "18rem", margin: "auto" }}>
      {breakdown.map((b, i) => (
        <ListGroup.Item key={i}>
          <span>{b.category} </span>
          <span className="total">{b.total}</span>
        </ListGroup.Item>
      ))}
    </ListGroup>
  );
}
