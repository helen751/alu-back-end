#!/usr/bin/python3
"""
A Python script that retrieves and displays the TODO list progress
for a given employee ID from a REST API (jsonplaceholder.typicode.com).
It accepts an integer as a command-line argument for the employee ID.
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches and prints the TODO list progress for a specific employee.

    Args:
        employee_id (int): The ID of the employee.
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        # 1. Fetch employee user information
        user_url = f"{base_url}/users/{employee_id}"
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        user_data = user_response.json()
        
        # Check if the user exists
        if not user_data:
            print(f"Error: Employee with ID {employee_id} not found.")
            return

        employee_name = user_data.get("name")

        # 2. Fetch employee's TODO list
        todos_url = f"{base_url}/todos?userId={employee_id}"
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        # Calculate progress
        total_tasks = len(todos_data)
        done_tasks = [task for task in todos_data if task.get("completed")]
        number_of_done_tasks = len(done_tasks)

        # 3. Display the progress
        # First line format: Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

        # Second and N next lines display the title of completed tasks
        for task in done_tasks:
            # Format: (1 tabulation and 1 space before the TASK_TITLE)
            print(f"\t {task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data: {e}", file=sys.stderr)
    except ValueError:
        print("Error: Invalid JSON response.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Check if an employee ID is provided as a command-line argument
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>", file=sys.stderr)
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.", file=sys.stderr)
        sys.exit(1)
