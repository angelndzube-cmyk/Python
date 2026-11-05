current_users = ['Admin', 'Sisipho', 'Jaden', 'Sarah', 'Mike']
new_users = ['john', 'SARAH', 'tom', 'admin', 'lisa']

# Make a lowercase copy of current_users for checking
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user}, that username is already taken. Please enter a new username.")
    else:
        print(f"Great {new_user}, that username is available!")