#!/usr/bin/python3
"""Accessing REST API for empplyee's to do list"""

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

    with open('{}.csv'.format(id_employee), 'w') as x:
        for task in work:
            x.write('"{}","{}","{}","{}"\n'
                    .format(id_employee, user, task.get('completed'),
                            task.get('title')))
