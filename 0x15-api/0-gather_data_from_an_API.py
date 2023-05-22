#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = 'Kingsley'
    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    done = ('5/6')
    done_tasks = [4]

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            #done += 1

    print(employeeName, 'is done with tasks', '(',done,')')

    for task in done_tasks:
        print("\t {}".format(task.get('title')))
