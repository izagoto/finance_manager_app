import React, { useState } from "react";
import {
  MDBContainer, MDBCol, MDBRow, MDBBtn,
  MDBIcon, MDBInput, MDBCheckbox
} from "mdb-react-ui-kit";
import API from "../../api/client";
import { useNavigate } from "react-router-dom";
import "./Login.css";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await API.post("/login", {
        username: username,
        password,
      }, {
        headers: {
          "Content-Type": "application/x-www-form-urlencoded"
        }
      });

      const token = response.data.data.access_token;
      localStorage.setItem("token", token);

      const decodeResponse = await API.get("/decode");
      console.log("Token valid. User:", decodeResponse.data.data);

      navigate("/dashboard");
    } catch (error) {
      alert("Login gagal: " + (error.response?.data?.message || error.message));
    }
  };

  return (
    <MDBContainer fluid className="p-3 my-5 h-custom">
      <MDBRow>
        <MDBCol col='10' md='6'>
          <img
            src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/draw2.webp"
            className="img-fluid"
            alt="Sample"
          />
        </MDBCol>

        <MDBCol col='4' md='6'>
          <div className="d-flex flex-row align-items-center justify-content-center">
            <p className="lead fw-normal mb-0 me-3">Sign in with</p>

            <MDBBtn floating size='md' tag='a' className='me-2'><MDBIcon fab icon='facebook-f' /></MDBBtn>
            <MDBBtn floating size='md' tag='a' className='me-2'><MDBIcon fab icon='twitter' /></MDBBtn>
            <MDBBtn floating size='md' tag='a' className='me-2'><MDBIcon fab icon='linkedin-in' /></MDBBtn>
          </div>

          <div className="divider d-flex align-items-center my-4">
            <p className="text-center fw-bold mx-3 mb-0">Or</p>
          </div>

          <MDBInput
            wrapperClass='mb-4'
            label='Username'
            id='form1'
            type='text'
            size="lg"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <MDBInput
            wrapperClass='mb-4'
            label='Password'
            id='form2'
            type='password'
            size="lg"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <div className="d-flex justify-content-between mb-4">
            <MDBCheckbox name='flexCheck' id='flexCheckDefault' label='Remember me' />
            <a href="#!">Forgot password?</a>
          </div>

          <div className='text-center text-md-start mt-4 pt-2'>
            <MDBBtn className="mb-0 px-5" size='lg' onClick={handleLogin}>
              Login
            </MDBBtn>
            <p className="small fw-bold mt-2 pt-1 mb-2">
              Don't have an account? <a href="#!" className="link-danger">Register</a>
            </p>
          </div>
        </MDBCol>
      </MDBRow>

      <div className="d-flex flex-column flex-md-row text-center text-md-start justify-content-between py-4 px-4 px-xl-5 bg-primary">
        <div className="text-white mb-3 mb-md-0">
          Copyright © 2020. All rights reserved.
        </div>

        <div>
          <MDBBtn tag='a' color='none' className='mx-3' style={{ color: 'white' }}>
            <MDBIcon fab icon='facebook-f' size="md" />
          </MDBBtn>
          <MDBBtn tag='a' color='none' className='mx-3' style={{ color: 'white' }}>
            <MDBIcon fab icon='twitter' size="md" />
          </MDBBtn>
          <MDBBtn tag='a' color='none' className='mx-3' style={{ color: 'white' }}>
            <MDBIcon fab icon='google' size="md" />
          </MDBBtn>
          <MDBBtn tag='a' color='none' className='mx-3' style={{ color: 'white' }}>
            <MDBIcon fab icon='linkedin-in' size="md" />
          </MDBBtn>
        </div>
      </div>
    </MDBContainer>
  );
};

export default Login;
