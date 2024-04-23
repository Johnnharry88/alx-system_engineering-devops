#!/usr/bin/python3
"""Getting a REST API for todo lists of employees"""


import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"

    res = requests.get(url)
    user = res.json()

    dict = {}
    for x in user:
        user_id = x.get('id')
        username = x.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        url = url + '/todos/'
        res = requests.get(url)
        work = res.json()
        dict[user_id] = []
        for task in work:
            dict[user_id].append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": username
                })
    with open('todo_all_employees.json', 'w') as x:
        json.dump(dict, x)
