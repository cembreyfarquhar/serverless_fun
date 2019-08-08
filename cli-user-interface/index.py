def app():
    while True:
        cmd = input('type your instruction then hit Enter\n')
        # Exit condition
        if cmd == 'q':
            break

if __name__ == "__main__":
    print("Hey ya!")
    app()