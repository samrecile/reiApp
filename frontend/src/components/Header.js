import React from 'react';

import { Navbar, Nav, Container } from 'react-bootstrap'
import { LinkContainer} from 'react-router-bootstrap'

const Header = () => {
  return (
    <header>
      <Navbar bg="primary" variant="dark" expand="lg" sticky="top" collapseOnSelect>
        <Container>
          <LinkContainer to='/'>
            <Navbar.Brand>Real Estate App</Navbar.Brand>
          </LinkContainer>
          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="mr-auto">

              <LinkContainer to='/'>
                <Nav.Link><i className="fas fa-shopping-cart"></i>Home</Nav.Link>
              </LinkContainer>

              <LinkContainer to="/">
                <Nav.Link><i className="fas fa-user"></i>Login</Nav.Link>
              </LinkContainer>
              
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
    </header>
  )
}

export default Header