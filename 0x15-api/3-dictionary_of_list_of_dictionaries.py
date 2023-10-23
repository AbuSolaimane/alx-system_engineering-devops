#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import json
import requests


if __name__ == '__main__':
    employeesUrl = "https://jsonplaceholder.typicode.com/users"
    employees = requests.get(employeeUrl).json()

    employees_tasks = {}
    for employee in employees:
        employeeId = employee.get('id')
        username = employee.get('username')

        todosUrl = employeesUrl + "/" + employeeId + "/todos"
        tasks = requests.get(todosUrl).json()
        employees_tasks[employeeId] = []
        for task in tasks:
            employees_tasks[employeeId].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
            })

    with open('todo_all_employees.json', 'w') as file:
                json.dump(employees_tasks, file)
