#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

Usage: ./0-gather_data_from_an_API.py <employee_id:int>

Outputs exactly:
Employee EMPLOYEE_NAME is done with tasks(DONE/TOTAL):
\t TASK_TITLE
...
"""

import sys
import requests


def main():
    if len(sys.argv) != 2:
        return

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        return

    base = "https://jsonplaceholder.typicode.com"

    # Fetch user (for name); if anything fails, just return (no noisy output)
    try:
        user = requests.get(f"{base}/users/{emp_id}", timeout=10).json()
        todos = requests.get(
            f"{base}/todos", params={"userId": emp_id}, timeout=10
        ).json()
    except Exception:
        return

    name = user.get("name", "")

    done_titles = [t.get("title", "")
                   for t in todos if t.get("completed") is True]

    total = len(todos)
    done = len(done_titles)

    # EXACT header line format
    print(f"Employee {name} is done with tasks({done}/{total}):")

    # EXACT line prefix for each completed task: tab + space
    for title in done_titles:
        print(f"\t {title}")


if __name__ == "__main__":
    main()
