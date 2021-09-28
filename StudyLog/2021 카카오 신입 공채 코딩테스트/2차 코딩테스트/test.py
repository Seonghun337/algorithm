import requests
import json


def getJsonTest():
    base = "https://jsonplaceholder.typicode.com/"
    detail = "posts"

    url = base+detail
    response = requests.get(url)
    print(response.text)


def main():
    pass

