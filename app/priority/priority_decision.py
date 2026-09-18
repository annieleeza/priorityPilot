def calculate_priority(task):
    score = 0

    # Importance
    importance_scores = {
        "Low": 10,
        "Medium": 20,
        "High": 30
    }

    score += importance_scores.get(task["importance"], 10)

    # Difficulty
    difficulty_scores = {
        "Easy": 5,
        "Medium": 10,
        "Hard": 15
    }

    score += difficulty_scores.get(task["difficulty"], 5)

    # Estimated time
    if task["estimated_hours"] >= 3:
        score += 15
    elif task["estimated_hours"] >= 1:
        score += 10
    else:
        score += 5

    # Deadline
    deadline = task["deadline"].lower()

    if "today" in deadline:
        score += 40
    elif "tomorrow" in deadline:
        score += 35
    elif "week" in deadline:
        score += 20
    else:
        score += 10

    return score


def get_priority_level(score):
    if score >= 80:
        return "HIGH"
    elif score >= 50:
        return "MEDIUM"
    else:
        return "LOW"
