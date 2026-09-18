from flask import Flask, jsonify, request

from app.priority.priority_gen import create_task
from app.priority.priority_decision import (
    calculate_priority,
    get_priority_level
)


def create_app():
    app = Flask(__name__)

    @app.route("/test", methods=["POST"])
    def test_priority():
        data = request.json

        task = create_task(
            data["name"],
            data["deadline"],
            data["estimated_hours"],
            data["importance"],
            data["difficulty"]
        )

        score = calculate_priority(task)
        level = get_priority_level(score)

        return jsonify({
            "task": task,
            "score": score,
            "priority": level
        })

    return app
