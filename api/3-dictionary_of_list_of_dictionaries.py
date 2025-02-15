#!/usr/bin/python3
"""
Export all employees' TODO lists to a JSON file.
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch all users
    users = requests.get(f"{url}users").json()

    # Dictionary to store all tasks
    all_tasks = {}

    # Fetch tasks for each user
    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        # Fetch todo list data
        todos = requests.get(f"{url}todos?userId={user_id}").json()

        # Prepare tasks
        tasks_list = [{"username": username, "task": task.get("title"), "completed": task.get("completed")} for task in todos]
        all_tasks[user_id] = tasks_list

    # Write to JSON file
    file_name = "todo_all_employees.json"
    with open(file_name, "w") as file:
        json.dump(all_tasks, file)
