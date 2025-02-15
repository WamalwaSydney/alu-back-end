import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"

    # Fetch user data
    user = requests.get(f"{url}users/{user_id}").json()
    username = user.get("username")

    # Fetch todo list data
    todos = requests.get(f"{url}todos?userId={user_id}").json()

    # Prepare JSON data
    tasks_list = [{"task": task.get("title"), "completed": task.get("completed"), "username": username} for task in todos]

    # Write to JSON file
    file_name = f"{user_id}.json"
    with open(file_name, "w") as file:
        json.dump({user_id: tasks_list}, file)
