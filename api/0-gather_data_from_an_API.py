#!/usr/bin/python3
"""
Gather data from an API and display employee TODO list progress.
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Fetches and displays employee TODO list progress.
    
    Args:
        employee_id (int): The employee ID
    """
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Get employee details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print(f"Error: Employee with ID {employee_id} not found.")
        return
    
    user_data = user_response.json()
    employee_name = user_data.get('name')
    
    # Get employee todos
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
    if todos_response.status_code != 200:
        print(f"Error: Could not fetch todos for employee {employee_id}.")
        return
    
    todos_data = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task.get('completed'))
    
    # Display progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    
    # Display completed tasks
    for task in todos_data:
        if task.get('completed'):
            print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
        sys.exit(1)