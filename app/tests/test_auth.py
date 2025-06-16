from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

test_user = {
    "username": "unittestuser",
    "full_name": "Unit Test",
    "email": "unittest@example.com",
    "password": "password",
    "role": "user",
}

access_token = None


def test_create_user():
    response = client.post("/api/create-user", json=test_user)
    json_data = response.json()
    print("CREATE USER:", json_data)
    assert response.status_code in [200, 400]


def test_login_user():
    global access_token

    response = client.post(
        "/api/login",
        data={
            "username": test_user["username"],
            "password": test_user["password"],
        },
        headers={"accept": "application/json"},
    )
    json_data = response.json()
    print("LOGIN RESPONSE:", json_data)

    assert response.status_code == 200
    assert "access_token" in json_data
    access_token = json_data["access_token"]


def test_decode_token():
    global access_token

    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("/api/decode", headers=headers)
    json_data = response.json()
    print("DECODE RESPONSE:", json_data)

    assert response.status_code == 200
    assert json_data["data"].get("sub") == test_user["username"]


def test_logout_user():
    global access_token

    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.post("/api/logout", headers=headers)
    json_data = response.json()
    print("LOGOUT RESPONSE:", json_data)

    assert response.status_code == 200
