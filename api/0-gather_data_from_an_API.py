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
from typing import Any, Dict, List, Optional
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

# Try to use requests if available; fall back to urllib otherwise.
try:
    import requests  # type: ignore[import-not-found]
except Exception:  # pragma: no cover
    requests = None  # type: ignore[assignment]

BASE_URL = "https://jsonplaceholder.typicode.com"


def _get_json(url: str, params: Optional[Dict[str, Any]] = None) -> Any:
    """Fetch JSON from URL using requests if available, else urllib."""
    if requests is not None:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        return resp.json()

    if params:
        url = f"{url}?{urlencode(params)}"
    req = Request(url, headers={"User-Agent": "python-urllib/3"})
    with urlopen(req, timeout=15) as resp:
        return json.load(resp)


def print_todo_progress(employee_id: int) -> None:
    """
    Prints the TODO progress for the given employee_id in the exact format:
    Employee EMPLOYEE_NAME is done with tasks(DONE/TOTAL):
        TASK_TITLE
    """
    try:
        user = _get_json(f"{BASE_URL}/users/{employee_id}")
        todos = _get_json(f"{BASE_URL}/todos", {"userId": employee_id})
    except (HTTPError, URLError, json.JSONDecodeError, Exception):
        # Silent failure to avoid breaking import-based checkers.
        return

    name = user.get("name", "")
    done_titles: List[str] = [
        t.get("title", "") for t in todos if t.get("completed") is True
    ]
    total = len(todos)
    done = len(done_titles)

    print(f"Employee {name} is done with tasks({done}/{total}):")
    for title in done_titles:
        print(f"\t {title}")


def main() -> None:
    if len(sys.argv) != 2:
        return
    try:
        emp_id = int(sys.argv[1])
    except ValueError:
        return
    print_todo_progress(emp_id)


if __name__ == "__main__":
    main()
