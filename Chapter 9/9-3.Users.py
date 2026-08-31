
class User:
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}, {self.age} years old, from {self.city}.")

    def greet_user(self):
        print(f"Hello {self.first_name}, welcome back!")

user1 = User("Sisipho", "Ndzube", 22, "Cape Town")
user2 = User("Liam", "Smith", 28, "Johannesburg")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()