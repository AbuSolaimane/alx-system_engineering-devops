#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    employeeUrl = "https://jsonplaceholder.typicode.com/users/" + employeeId
    employee = requests.get(employeeUrl).json()
    employeeUsername = employee.get('username')

    todosUrl = employeeUrl + "/todos"
    tasks = requests.get(todosUrl).json()

    with open('{}.csv'.format(employeeId), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(employeeId, employeeUsername, task.get('completed'),
                               task.get('title')))

