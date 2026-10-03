from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert b"Task Manager" in response.data


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"
    assert data["environment"] == "QA"


def test_get_tasks():
    client = app.test_client()

    response = client.get("/api/tasks")

    assert response.status_code == 200

    data = response.get_json()

    assert len(data) >= 2


def test_create_task():
    client = app.test_client()

    response = client.post(
        "/api/tasks",
        json={"title": "Test GitHub Actions"}
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["title"] == "Test GitHub Actions"
    assert data["completed"] is False