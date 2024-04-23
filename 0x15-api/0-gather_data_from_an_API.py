#!/usr/bin/python3
"""Accessing REST API for empplyee's to do list"""

import requests
import sys

if __name__ == "__main__":
    id_employee = sys.argv[1]
    access_url = "https://jsonplaceholder.typicode.com/users"
    url = access_url + '/' + id_employee

    response = requests.get(url)
    employee_name = response.json().get('name')

    url_toddo = url + '/todos'
    response = requests.get(url_toddo)
    work = response.json()
    done = 0
    task_done = []
    for task in work:
        if task.get('completed'):
            task_done.append(task)
            done = done + 1
    print("Employee {} is done with tasks ({}/{}):"
          .format(employee_name, done, len(work)))
    for task in task_done:
        print("\t {}".format(task.get('title')))
