import React, { useState } from "react";
import Container from "react-bootstrap/Container";
import { Navbar, Button } from "react-bootstrap";
import Login from "./Login";

export default function NavBar() {
  const [modalShow, setModalShow] = React.useState(false);

  return (
    <>
      <Navbar bg="dark" variant="dark">
        <Container>
          <Navbar.Brand href="#home">DQRCG</Navbar.Brand>
          <Navbar.Toggle />
          <Navbar.Collapse className="justify-content-end">
            <Button variant="primary" onClick={() => setModalShow(true)}>
              SIGN IN<a href="#login"></a>
            </Button>
            <Login show={modalShow} onHide={() => setModalShow(false)} />
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </>
  );
}
