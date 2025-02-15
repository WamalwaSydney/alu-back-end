#!/usr/bin/python3
"""
Gather data from an API and display the completed tasks of an employee.
"""

import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user = requests.get(f"{url}users/{user_id}").json()
    user_name = user.get("name")

    # Fetch todo list data
    todos = requests.get(f"{url}todos?userId={user_id}").json()
    
    # Filter completed tasks
    done_tasks = [task for task in todos if task.get("completed")]

    # Print progress
    print(f"Employee {user_name} is done with tasks({len(done_tasks)}/{len(todos)}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
