from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory task store
tasks = []

@app.get("/")
def home():
    return jsonify({"message": "To-Do List API is running!"})

@app.post("/tasks")
def add_task():
    data = request.get_json()

    # Generate ID based on current list size
    task = {
        "id": len(tasks) + 1,
        "title": data.get("title", ""),
        "completed": False
    }

    tasks.append(task)
    return jsonify(task), 201

@app.get("/tasks")
def list_tasks():
    return jsonify(tasks), 200

@app.put("/tasks/<int:id>")
def update_task(id):
    for task in tasks:
        if task["id"] == id:
            data = request.get_json()
            task["title"] = data.get("title", task["title"])
            task["completed"] = data.get("completed", task["completed"])
            return jsonify(task), 200
    return jsonify({"error": "Task not found"}), 404

@app.delete("/tasks/<int:id>")
def delete_task(id):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
