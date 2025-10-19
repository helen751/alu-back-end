#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

For a given employee ID, prints TODO progress in the exact format:
Employee EMPLOYEE_NAME is done with tasks(DONE/TOTAL):
\t TASK_TITLE
...
"""

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


BASE_URL = "https://jsonplaceholder.typicode.com"


def fetch_json(url):
    """Fetch JSON from URL using urllib and return parsed object."""
    req = Request(url, headers={"User-Agent": "python-urllib/3"})
    with urlopen(req, timeout=10) as resp:
        return json.load(resp)


def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    try:
        user = fetch_json(f"{BASE_URL}/users/{emp_id}")
        todos = fetch_json(f"{BASE_URL}/todos?userId={emp_id}")
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError):
        sys.exit(1)

    name = user.get("name", "")
    done_titles = [t.get("title", "")
                   for t in todos if t.get("completed") is True]
    total = len(todos)
    done = len(done_titles)

    # First line: exact wording and punctuation
    print(f"Employee {name} is done with tasks({done}/{total}):")

    # Each completed task title: one tab + one space before the title
    for title in done_titles:
        print(f"\t {title}")


if __name__ == "__main__":
    main()
