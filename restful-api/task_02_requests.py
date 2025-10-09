#!/usr/bin/python
"""
"""


import requests
import csv
import json


def fetch_and_print_posts():
    """
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.status_code == 200:
        print("Status Code: 200")
        data = response.json()
        if isinstance(data, list):
            titles = [item.get("title") for item in data if "title" in item]
        elif isinstance(data, dict):
            titles = [data.get("title")]
        else:
            titles = []
        for title in titles:
            print(title)
    else:
        return


def fetch_and_save_posts():
    """
    """
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    if response.status_code != 200:
        return

    data = response.json()
    if isinstance(data, dict):
        data = [data]
    elif not isinstance(data, list):
        return

    data_dict = [
        {
            "id": item.get("id"),
            "title": item.get("title"),
            "body": item.get("body", "")
        }
        for item in data
        if isinstance(item, dict)
    ]
    headers = ["id", "title", "body"]
    with open("posts.csv", 'w', encoding='utf-8') as csvfile:
        write = csv.DictWriter(csvfile, fieldnames=headers)
        write.writeheader()
        write.writerows(data_dict)
