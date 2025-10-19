#!/usr/bin/python3
"""Gather TODO data from JSONPlaceholder and print progress for one employee.

Usage:
    ./0-gather_data_from_an_API.py <employee_id:int>

Output format:
    Employee EMPLOYEE_NAME is done with tasks(DONE/TOTAL):
        \t TASK_TITLE
        \t TASK_TITLE
        ...
(Only completed tasks are listed. The prefix is one tab then one space.)
"""

import sys
import requests


API = "https://jsonplaceholder.typicode.com"


def main() -> None:
    """Fetch one user's TODOs and print completion summary."""
    if len(sys.argv) != 2:
        return

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        return

    user_url = f"{API}/users/{user_id}"
    todos_url = f"{API}/todos"

    user_resp = requests.get(user_url)
    if user_resp.status_code != 200:
        return
    user = user_resp.json()
    employee_name = user.get("name", "")

    todos_resp = requests.get(todos_url, params={"userId": user_id})
    if todos_resp.status_code != 200:
        return
    todos = todos_resp.json()

    total = len(todos)
    done_tasks = [t for t in todos if bool(t.get("completed"))]
    done_count = len(done_tasks)

    # Exact first-line formatting (no extra spaces)
    print(
        f"Employee {employee_name} is done with tasks({done_count}/{total}):"
    )

    # Each completed task on its own line, exactly: tab + space + title
    for t in done_tasks:
        title = t.get("title", "")
        print(f"\t {title}")


if __name__ == "__main__":
    main()
