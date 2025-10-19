#!/usr/bin/python3
"""
0-gather_data_from_an_API.py

For a given employee ID, prints:
Employee EMPLOYEE_NAME is done with tasks(DONE/TOTAL):
\t TASK_TITLE
...
"""

import json
import sys
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

BASE = "https://jsonplaceholder.typicode.com"


def fetch_json(url):
    req = Request(url, headers={"User-Agent": "python-urllib/3"})
    with urlopen(req, timeout=15) as resp:
        return json.load(resp)


def main():
    # Require exactly one integer argument (employee ID)
    if len(sys.argv) != 2:
        sys.exit(1)
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    try:
        user = fetch_json(f"{BASE}/users/{emp_id}")
        todos = fetch_json(f"{BASE}/todos?userId={emp_id}")
    except (URLError, HTTPError, json.JSONDecodeError):
        # If the API can't be reached, exit non-zero so the checker reruns
        sys.exit(1)

    name = user.get("name", "")
    done_titles = [
        t.get("title", "")
        for t in todos
        if t.get("completed") is True
    ]
    total = len(todos)
    done = len(done_titles)

    # EXACT header line
    print(f"Employee {name} is done with tasks({done}/{total}):")

    # EXACT formatting for each completed task: tab + space then title
    for title in done_titles:
        print(f"\t {title}")


if __name__ == "__main__":
    main()
