import { Button, Modal, Form, Row, Col, Alert } from "react-bootstrap";
import React, { useState, useEffect } from "react";
import config from "../config";
import axios from "axios";

export default function Login(props) {
  const [variant, setVariant] = useState("danger");
  const [show, setShow] = useState(false);

  const handleLogin = (e) => {
    e.preventDefault();
    startLogin();
  };

  function startLogin() {
    axios
      .get(config.BASE_URL + "login")
      .then((res) => {
        console.log("started login");
      })
      .catch((err) => {
        console.log("errdata");
        // seterrData(err.response.data.error);
      });
  }

  return (
    <Modal
      {...props}
      size="lg"
      aria-labelledby="contained-modal-title-vcenter"
      centered
    >
      <Modal.Header closeButton>
        <Modal.Title id="contained-modal-title-vcenter">
          Sign in to continue
        </Modal.Title>
      </Modal.Header>
      <Modal.Body>
        <Form>
          <Row>
            <Col>
              {show && (
                <Alert variant={variant} onClose={() => setShow(false)}>
                  This is a {variant} alert—check it out!
                </Alert>
              )}
              <Form.Label>Account</Form.Label>
            </Col>
            <Col xs={5}>
              <Button variant="outline-secondary" onClick={handleLogin}>
                Sign in with Google
              </Button>
            </Col>
          </Row>
          <Row>
            <Col>
              <Form.Control placeholder="username or email" />
            </Col>
            <Col xs={5}>
              <Button variant="outline-secondary">Sign in with Github</Button>
            </Col>
          </Row>

          <Row>
            <Col>
              <Form.Label>Password</Form.Label>
            </Col>
          </Row>

          <Row>
            <Col xs={6}>
              <Form.Control placeholder="password" />
            </Col>
          </Row>

          <Button variant="primary" type="submit" onClick={handleLogin}>
            Continue
          </Button>
        </Form>
      </Modal.Body>
      <Modal.Footer>
        <Button onClick={props.onHide}>Close</Button>
      </Modal.Footer>
    </Modal>
  );
}
