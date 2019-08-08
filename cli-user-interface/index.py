logged_in = False

def auth():
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