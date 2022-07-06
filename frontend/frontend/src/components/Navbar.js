import React from "react";
import { Link, NavLink } from "react-router-dom";
import { useSelector } from 'react-redux';

const Navbar = () => {
  const { isAuthenticated } = useSelector(state => state.user);

  const authLinks = (
    <>
      <li class="nav-item">
        <NavLink className="nav-link" to="/dashboard">
          Dashboard
        </NavLink>
      </li>
      <li class="nav-item">
        <a href='#!' className="nav-link">
          Logout
        </a>
      </li>
    </>
  );

  const guestLinks = (
    <>
      <li class="nav-item">
        <NavLink className="nav-link" to="/login">
          Login
        </NavLink>
      </li>
      <li class="nav-item">
        <NavLink className="nav-link" to="/register">
          Register
        </NavLink>
      </li>
    </>
  );

  return (
    <nav class="navbar navbar-dark bg-primary">
      <div class="container-fluid">
        <Link className="navbar-brand" to="/">
          REI Site
        </Link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav">
            <li class="nav-item">
              <NavLink className="nav-link" to="/">
                Home
              </NavLink>
            </li>
            { isAuthenticated ? authLinks : guestLinks}
          </ul>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
