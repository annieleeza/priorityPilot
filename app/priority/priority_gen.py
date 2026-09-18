def create_task(name, deadline, estimated_hours, importance, difficulty):
    task = {
        "name": name,
        "deadline": deadline,
        "estimated_hours": estimated_hours,
        "importance": importance,
        "difficulty": difficulty
    }

    return task
