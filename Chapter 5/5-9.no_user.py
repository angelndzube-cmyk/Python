usernames = ['admin', 'sisipho', 'jaden', 'sarah', 'mike']

if usernames:  # checks if list is not empty
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    print("We need to find some users!")

# Test with empty list
usernames = []
if usernames:
    for username in usernames:
        print(username)
else:
    print("We need to find some users!")