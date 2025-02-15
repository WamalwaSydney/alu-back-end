import csv
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

    # Write to CSV
    file_name = f"{user_id}.csv"
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([user_id, username, task.get("completed"), task.get("title")])

