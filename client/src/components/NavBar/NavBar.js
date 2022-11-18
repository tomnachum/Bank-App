import React from "react";
import "./NavBar.css";
import Container from "react-bootstrap/Container";
import Nav from "react-bootstrap/Nav";
import Navbar from "react-bootstrap/Navbar";
import { NavLink } from "react-router-dom";

export default function NavBar() {
  return (
    <Navbar bg="light" expand="lg">
      <Navbar.Brand style={{ marginLeft: "20px" }}>Bank App</Navbar.Brand>
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
        <Navbar.Text>Balance:</Navbar.Text>
      </Navbar.Collapse>
    </Navbar>
  );
}
