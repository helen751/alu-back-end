#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

Fetches an employee's TODO progress from JSONPlaceholder and prints it in the
required format:

Employee EMPLOYEE_NAME is done with tasks(DONE/TOTAL):
\t TASK_TITLE
\t TASK_TITLE
...
"""

import requests
import sys


def main():
    if len(sys.argv) != 2:
        # Expect exactly one integer argument (employee ID)
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Get employee (user) info
    user_url = f"{base_url}/users/{emp_id}"
    try:
        user_resp = requests.get(user_url, timeout=10)
        user_resp.raise_for_status()
    except requests.RequestException:
        sys.exit(1)

    user = user_resp.json()
    emp_name = user.get("name", "")

    # Get todos for this user
    todos_url = f"{base_url}/todos"
    try:
        todos_resp = requests.get(
            todos_url, params={"userId": emp_id}, timeout=10
        )
        todos_resp.raise_for_status()
    except requests.RequestException:
        sys.exit(1)

    todos = todos_resp.json()
    done_titles = [t.get("title", "")
                   for t in todos if t.get("completed") is True]

    total = len(todos)
    done = len(done_titles)

    # First line EXACT format
    print(f"Employee {emp_name} is done with tasks({done}/{total}):")

    # Completed task titles, each with a leading tab then a space
    for title in done_titles:
        print(f"\t {title}")


if __name__ == "__main__":
    main()
