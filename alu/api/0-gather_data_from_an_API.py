#!/usr/bin/python3
"""
Module 0-gather_data_from_an_API
Fetches an employee's TODO list from JSONPlaceholder and prints
progress in the required format.
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
    user = requests.get(f"{base}/users/{user_id}").json()
    todos = requests.get(f"{base}/todos", params={"userId": user_id}).json()

    name = user.get("name")
    total = len(todos)
    done_tasks = [t for t in todos if t.get("completed")]
    done_count = len(done_tasks)

    print(f"Employee {name} is done with tasks({done_count}/{total}):")
    for task in done_tasks:
        title = task.get("title")
        print(f"\t {title}")


if __name__ == "__main__":
    main()
