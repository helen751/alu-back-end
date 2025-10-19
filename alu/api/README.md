# API — JSONPlaceholder Tasks

This folder contains solutions for the ALU/holberton **API** project
using the JSONPlaceholder REST API.

## Files

- `0-gather_data_from_an_API.py` — prints an employee’s TODO progress.
- `1-export_to_CSV.py` — exports that employee’s tasks to `USER_ID.csv`.
- `2-export_to_JSON.py` — exports that employee’s tasks to `USER_ID.json`.
- `3-dictionary_of_list_of_dictionaries.py` — exports all users’ tasks
  to `todo_all_employees.json`.

## Notes
- First line has the correct shebang (`#!/usr/bin/python3`).
- Modules are documented, imports are **alphabetically** ordered.
- Code formatted to be PEP8-friendly.
- Uses `requests` to consume the API:
  - Users: `https://jsonplaceholder.typicode.com/users/{id}`
  - Todos: `https://jsonplaceholder.typicode.com/todos?userId={id}`
