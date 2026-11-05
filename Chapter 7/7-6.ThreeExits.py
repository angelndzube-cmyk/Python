

# Version 1: Conditional test in while statement
print("Version 1 - Conditional test:")
topping = ""
while topping != 'quit':
    topping = input("Enter a topping (quit to stop): ")
    if topping != 'quit':
        print(f"I'll add {topping}.")

# Version 2: Active variable
print("\nVersion 2 - Active variable:")
active = True
while active:
    topping = input("Enter a topping (quit to stop): ")
    if topping == 'quit':
        active = False
    else:
        print(f"I'll add {topping}.")

# Version 3: Break statement
print("\nVersion 3 - Break statement:")
while True:
    topping = input("Enter a topping (quit to stop): ")
    if topping == 'quit':
        break
    print(f"I'll add {topping}.")