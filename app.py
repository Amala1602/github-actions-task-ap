from flask import Flask, jsonify, request

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Learn GitHub Actions", "completed": False},
    {"id": 2, "title": "Deploy to Azure", "completed": False},
]


@app.route("/")
def home():
    return """
    <h1>Task Manager</h1>
    <p>Application is running.</p>
    <p>CI/CD: GitHub Actions → Docker → Azure App Service</p>
    """


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "environment": "QA"
    })


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)


@app.route("/api/tasks", methods=["POST"])
def create_task():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "title is required"}), 400

    new_task = {
        "id": len(tasks) + 1,
        "title": data["title"],
        "completed": False
    }

    tasks.append(new_task)

    return jsonify(new_task), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)