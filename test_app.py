import json
from app import app, tasks

def setup_function():
    tasks.clear()

def test_home():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert res.json["message"] == "To-Do List API is running!"

def test_add_task():
    client = app.test_client()
    res = client.post("/tasks", json={"title": "Buy milk"})
    assert res.status_code == 201
    assert res.json["title"] == "Buy milk"

def test_list_tasks():
    client = app.test_client()
    client.post("/tasks", json={"title": "Buy milk"})
    res = client.get("/tasks")
    assert res.status_code == 200
    assert len(res.json) == 1

def test_update_task():
    client = app.test_client()
    client.post("/tasks", json={"title": "Buy milk"})
    res = client.put("/tasks/1", json={"completed": True})
    assert res.status_code == 200
    assert res.json["completed"] is True

def test_delete_task():
    client = app.test_client()
    client.post("/tasks", json={"title": "Buy milk"})
    res = client.delete("/tasks/1")
    assert res.status_code == 200
