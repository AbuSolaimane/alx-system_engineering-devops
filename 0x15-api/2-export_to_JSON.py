#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    employeeUrl = "https://jsonplaceholder.typicode.com/users/" + employeeId
    employee = requests.get(employeeUrl).json()
    employeeUsername = employee.get('username')

    todosUrl = employeeUrl + "/todos"
    tasks = requests.get(todosUrl).json()

    employee_tasks = {employeeId: []}
    for task in tasks:
        employee_tasks[employeeId].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employeeUsername
        })
    with open('{}.json'.format(employeeId), 'w') as file:
        json.dump(employee_tasks, file)
