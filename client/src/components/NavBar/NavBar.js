import React from "react";
import "./NavBar.css";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import { NavLink } from "react-router-dom";
import Balance from "./Balance/Balance";

export default function NavBar(props) {
  return (
    <Navbar bg="dark" expand="lg" variant="dark">
      <Navbar.Brand style={{ marginLeft: "20px" }}>
        <img
          src="https://cdn.icon-icons.com/icons2/1149/PNG/512/1486504348-business-coins-finance-banking-bank-marketing_81341.png"
          className="logo"
        />
        Bank App
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto">
          <Nav.Link as={NavLink} to="/transactions">
            Transactions
          </Nav.Link>
          <Nav.Link as={NavLink} to="/operations">
            Operations
          </Nav.Link>
          <Nav.Link as={NavLink} to="/breakdown">
            Breakdown
          </Nav.Link>
        </Nav>
      </Navbar.Collapse>
      <Navbar.Collapse
        style={{ marginRight: "20px" }}
        className="justify-content-end"
      >
        <Navbar.Text>
          <Balance balance={props.balance}></Balance>
        </Navbar.Text>
      </Navbar.Collapse>
    </Navbar>
  );
}
