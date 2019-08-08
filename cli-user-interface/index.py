import requests
import json
import os

logged_in = False

def auth():
    try:
        print(os.environ['AUTH_URL'])
        url = os.environ['AUTH_URL']
    except KeyError:
        print("AUTH_URL environment variable is not set")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    global logged_in
    if username == 'test':
        logged_in = True

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