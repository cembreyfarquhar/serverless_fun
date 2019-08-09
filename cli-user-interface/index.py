import requests
import json
import os

from env import LAMBDAS

logged_in = False

def auth():
    global url
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    headers = {"content-type": "application/json"}

    body = {
        "username": username,
        "password": password
    }

    response = requests.post(f"{url}/auth", json=body, headers=headers).json()

    print(response)
    global logged_in
    if "username" in response:
        logged_in = True
    else:
        print("Invalid credentials")

def app():
    while True:
        cmd = input('type your instruction then hit Enter\n')
        # Exit condition
        if cmd == 'q':
            break
        elif len(cmd.split(' ')) == 3:
            print("You entered: " + cmd)
            add(cmd)
        else:
            print("not a valid expression, must be in form (number operation number)")

def add(cmd):
    global url
    
    inputs = cmd.split(" ")
    print(inputs[0])
    body = {
        "x": int(inputs[0]),
        "y": int(inputs[2])
    }

    headers = {"content-type": "application/json"}

    response = requests.post(f"{url}/add", json=body, headers=headers).json()

    print(response)

if __name__ == "__main__":
    print("Hey ya!")
    try:
        url = os.environ["LAMBDAS"] = LAMBDAS
    except KeyError:
        print("AUTH_URL environment variable is not set")
    while not logged_in:
        auth()
    app()