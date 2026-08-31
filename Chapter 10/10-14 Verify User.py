
import json

def get_new_username():
    username = input("What is your username? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return get_new_username()

    answer = input(f"Are you {username}? (yes/no): ")
    if answer == 'yes':
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We will remember you, {username}!")

    return username

greet_user()