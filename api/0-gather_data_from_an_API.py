#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

For a given employee ID, prints:
Employee EMPLOYEE_NAME is done with tasks(DONE/TOTAL):
\t TASK_TITLE
...
"""

import requests
import sys


BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_user(emp_id):
    """Return user object or {} on failure."""
    try:
        r = requests.get(f"{BASE_URL}/users/{emp_id}", timeout=10)
        r.raise_for_status()
        return r.json() or {}
    except Exception:
        return {}


def fetch_todos(emp_id):
    """Return list of todos or [] on failure."""
    try:
        r = requests.get(
            f"{BASE_URL}/todos", params={"userId": emp_id}, timeout=10
        )
        r.raise_for_status()
        data = r.json()
        return data if isinstance(data, list) else []
    except Exception:
        return []


def print_todo_progress(emp_id):
    """Print progress in the exact required format."""
    user = fetch_user(emp_id)
    todos = fetch_todos(emp_id)

    name = user.get("name", "")
    done_titles = [t.get("title", "") for t in todos if t.get("completed")]
    total = len(todos)
    done = len(done_titles)

    print(f"Employee {name} is done with tasks({done}/{total}):")
    for title in done_titles:
        print(f"\t {title}")


def main():
    if len(sys.argv) != 2:
        return
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        return
    print_todo_progress(emp_id)


if __name__ == "__main__":
    main()
