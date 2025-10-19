#!/usr/bin/python3
"""
0-gather_data_from_an_API
Fetch an employee's TODO list from JSONPlaceholder and print progress.

Usage:
  ./0-gather_data_from_an_API.py <employee_id:int>
"""
import requests
import sys


def main():
    """Entry point: parse user id, query API, and print progress."""
    if len(sys.argv) < 2:
        sys.exit(0)

    try:
        user_id = int(sys.argv[1])
    except ValueError:
        sys.exit(0)

    base = "https://jsonplaceholder.typicode.com"

    # Fetch user (for the employee name)
    user_resp = requests.get(f"{base}/users/{user_id}", timeout=10)
    user_resp.raise_for_status()
    user = user_resp.json()
    name = user.get("name")

    # Fetch todos for that user
    todos_resp = requests.get(f"{base}/todos", params={"userId": user_id}, timeout=10)
    todos_resp.raise_for_status()
    todos = todos_resp.json()

    total = len(todos)
    done_tasks = [t for t in todos if t.get("completed") is True]
    done_count = len(done_tasks)

    # Exact formatting required by checker
    print(f"Employee {name} is done with tasks({done_count}/{total}):")
    for task in done_tasks:
        title = task.get("title")
        print(f"\t {title}")


if __name__ == "__main__":
    main()
