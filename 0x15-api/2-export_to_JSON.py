#!/usr/bin/python3
"""Accessing REST API for empplyee's to do list"""

import json
import requests
import sys


if __name__ == "__main__":
    id_employee = sys.argv[1]
    access_url = "https://jsonplaceholder.typicode.com/users"
    url = access_url + '/' + id_employee

    response = requests.get(url)
    user = response.json().get('username')

    url_toddo = url + '/todos'
    response = requests.get(url_toddo)
    work = response.json()

    dict = {id_employee: []}
    for task in work:
        dict[id_employee].append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user
            })
    with open('{}.json'.format(id_employee), 'w') as x:
        json.dump(dict, x)
