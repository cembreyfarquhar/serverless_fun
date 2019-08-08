import requests
import json
import os

from env import AUTH_URL

logged_in = False

def auth():
    try:
        url = os.environ['AUTH_URL'] = AUTH_URL
    except KeyError:
        print("AUTH_URL environment variable is not set")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    headers = {"content-type": "application/json"}

    body = {
        "username": username,
        "password": password
    }

    response = requests.post(url, json=body, headers=headers).json()

    print(response)
    global logged_in
    if response["username"]:
        logged_in = True
    else:
        print("Invalid credentials")

def app():
    while True:
        cmd = input('type your instruction then hit Enter\n')
        # Exit condition
        if cmd == 'q':
            break
        else:
            print("You entered: " + cmd)

if __name__ == "__main__":
    print("Hey ya!")
    while not logged_in:
        auth()
    app()