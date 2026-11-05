
import json

username = input("What is your username? ")
age = input("How old are you? ")
city = input("Where do you live? ")

user_info = {
    'username': username,
    'age': age,
    'city': city
}

filename = 'user_info.json'
with open(filename, 'w') as f:
    json.dump(user_info, f)

with open(filename) as f:
    loaded_info = json.load(f)

print("\nI remember this about you:")
print(f"Username: {loaded_info['username']}")
print(f"Age: {loaded_info['age']}")
print(f"City: {loaded_info['city']}")