#!/usr/bin/python3
"""
A Python script that, for a given employee ID, returns information
about his/her TODO list progress using a REST API.
"""

import requests
import sys

if __name__ == "__main__":
    # Ensure an employee ID is provided as an argument
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    # Ensure the provided ID is an integer
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user information to get the employee's name
    user_url = "{}/users/{}".format(base_url, employee_id)
    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()  # Raise an HTTPError for bad responses
        user_data = user_response.json()
        employee_name = user_data.get("name")
    except requests.exceptions.RequestException as e:
        print("Error fetching user data: {}".format(e))
        sys.exit(1)
    except ValueError:
        print("Error: Could not decode JSON from user data response.")
        sys.exit(1)

    # Fetch the TODO list for the specified employee using query parameters
    todos_url = "{}/todos".format(base_url)
    params = {"userId": employee_id}
    try:
        todos_response = requests.get(todos_url, params=params)
        todos_response.raise_for_status()
        todos_data = todos_response.json()
    except requests.exceptions.RequestException as e:
        print("Error fetching TODO data: {}".format(e))
        sys.exit(1)
    except ValueError:
        print("Error: Could not decode JSON from TODO list response.")
        sys.exit(1)

    # Process the tasks to find completed ones
    completed_tasks = [task for task in todos_data if task.get("completed")]
    number_of_done_tasks = len(completed_tasks)
    total_number_of_tasks = len(todos_data)

    # Display the result in the specified format
    if employee_name and todos_data is not None:
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done_tasks, total_number_of_tasks))

        for task in completed_tasks:
            print("\t {}".format(task.get("title")))
