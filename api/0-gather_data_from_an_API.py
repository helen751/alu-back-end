#!/usr/bin/python3
"""Gather TODO data from a REST API and print progress for a given employee.

Usage:
    ./0-gather_data_from_an_API.py <employee_id:int>

Output format:
    Employee EMPLOYEE_NAME is done with tasks(DONE/TOTAL):
        \t TASK_TITLE
        \t TASK_TITLE
        ...
(Only completed tasks are listed.)
"""

import requests
import sys


API = "https://jsonplaceholder.typicode.com"


def main() -> None:
    """Entry point: fetch a user's TODOs and print progress."""
    if len(sys.argv) != 2:
        sys.exit(0)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        sys.exit(0)

    user_resp = requests.get(f"{API}/users/{user_id}", timeout=10)
    if user_resp.status_code != 200:
        sys.exit(0)
    user = user_resp.json()
    employee_name = user.get("name", "")

    todos_resp = requests.get(f"{API}/todos", params={"userId": user_id}, timeout=10)
    if todos_resp.status_code != 200:
        sys.exit(0)
    todos = todos_resp.json()

    total = len(todos)
    done_tasks = [t for t in todos if t.get("completed") is True]
    done_count = len(done_tasks)

    # Exact first-line formatting
    print(f"Employee {employee_name} is done with tasks({done_count}/{total}):")

    # Each completed task on its own line, prefixed by a tab and a space
    for t in done_tasks:
        title = t.get("title", "")
        print(f"\t {title}")


if __name__ == "__main__":
    main()
