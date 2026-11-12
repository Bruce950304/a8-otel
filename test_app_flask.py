from app_flask import app


def test_checkout_returns_paid():
    client = app.test_client()
    response = client.get("/checkout")
    assert response.status_code == 200
    assert response.data == b"paid\n"
