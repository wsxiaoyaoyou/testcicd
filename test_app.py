from app import app
def test_ping():
    resp = app.test_client().get("/api/ping")
    assert resp.status_code == 200
    assert resp.json["ping"] == "pong"