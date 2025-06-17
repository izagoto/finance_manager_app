import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../../api/client";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async () => {
    try {
      const response = await API.post(
        "/login",
        { username, password },
        {
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
        }
      );

      const token = response.data.data.access_token;
      localStorage.setItem("token", token);

      const decodeResponse = await API.get("/decode");
      console.log("Token valid. User:", decodeResponse.data.data);

      navigate("/dashboard");
    } catch (error) {
      alert(
        "Login gagal: " +
        (error.response?.data?.message || error.message)
      );
    }
  };

  return (
    <main className="main-content min-vh-100 d-flex align-items-center" style={{ backgroundColor: "#f0f0f0" }}>
      <div className="container mb-12">
        <div className="row justify-content-center">
          <div className="col-lg-4 col-md-6 col-12">
            <div className="card shadow-lg rounded-4 border-0" style={{ backgroundColor: "#ffffff", overflow: "hidden" }}>
              <div className="p-4" style={{ background: "linear-gradient(135deg, #FFFFFF, #f3f3f3)" }}>
                <h4 className="text-dark text-center m-0 fw-bold" >Sign in</h4>
              </div>
              <div className="card-body px-4 py-4">
                <form className="text-start" onSubmit={(e) => e.preventDefault()}>
                  <div className="form-group mb-3">
                    <label className="form-label">Username</label>
                    <input type="text" className="form-control" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Enter your username" />
                  </div>
                  <div className="form-group mb-3">
                    <label className="form-label">Password</label>
                    <input type="password" className="form-control" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Enter your password" />
                  </div>
                  <div className="text-center">
                    <button type="button" className="btn w-100 text-white" style={{ backgroundColor: "#16BBB9" }} onClick={handleLogin}>
                      Sign in
                    </button>
                  </div>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
};

export default Login;
