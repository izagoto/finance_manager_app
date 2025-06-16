// src/components/Dashboard.jsx
import React, { useEffect, useState } from "react";
import API from "../api/client";
import { useNavigate } from "react-router-dom";
import {
  MDBContainer,
  MDBBtn,
  MDBCard,
  MDBCardBody,
  MDBCardTitle,
  MDBSpinner,
  MDBIcon,
} from "mdb-react-ui-kit";

function Dashboard() {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  useEffect(() => {
    API.get("/decode")
      .then((res) => {
        setUser(res.data.data);
        setLoading(false);
      })
      .catch(() => {
        logout();
      });
  }, []);

  if (loading) {
    return (
      <MDBContainer className="d-flex justify-content-center align-items-center" style={{ height: "100vh" }}>
        <MDBSpinner grow color="primary">
          <span className="visually-hidden">Loading...</span>
        </MDBSpinner>
      </MDBContainer>
    );
  }

  return (
    <MDBContainer className="mt-5">
      <MDBCard alignment="center">
        <MDBCardBody>
          <MDBCardTitle className="mb-4">
            <h3>Dashboard</h3>
          </MDBCardTitle>
          <p className="lead">Welcome, <strong>{user.sub}</strong>!</p>
          <MDBBtn color="danger" onClick={logout}>
            <MDBIcon icon="sign-out-alt" className="me-2" />
            Logout
          </MDBBtn>
        </MDBCardBody>
      </MDBCard>
    </MDBContainer>
  );
}

export default Dashboard;
