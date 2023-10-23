#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    employeeUrl = "https://jsonplaceholder.typicode.com/users/" + employeeId

    employee = requests.get(employeeUrl).json()
    employeeName = employee.get('name')

    todosUrl = employeeUrl + "/todos"
    tasks = requests.get().json()
    done_tasks = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, done, len(tasks)))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
