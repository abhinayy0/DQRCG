import React from 'react';
import Container from 'react-bootstrap/Container';
import { Navbar } from 'react-bootstrap';

export default function NavBar() {
  return (
    <>
 <Navbar bg="dark" variant="dark">
  <Container>
    <Navbar.Brand href="#home">DQRCG</Navbar.Brand>
    <Navbar.Toggle />
    <Navbar.Collapse className="justify-content-end">
      <Navbar.Text>
        Login/Signup <a href="#login"></a>
      </Navbar.Text>
    </Navbar.Collapse>
  </Container>
</Navbar>
  </>
  )
};
