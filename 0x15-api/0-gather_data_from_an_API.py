#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    id_employee = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + id_employee

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo = url + "/todos"
    response = requests.get(todo)
    work = response.json()
    done = 0
    tasks_done = []

    for task in work:
        if task.get('completed'):
            task_done.append(task)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, done, len(work)))

    for task in tasks_done:
        print("\t {}".format(task.get('title')))
