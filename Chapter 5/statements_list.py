#Creating a variable called available_items that has a list of items as values
available_items = ["Banana", "Cherry", "Peach", "Lemon", "Apple", "Guava", "Mango"]

#Creating a variable called shopping_cart that has an empty list as a value
#That will store the items later
shopping_cart = []

#Using the input() method to prompt users to enter their value
#Creating 3 variables (item1, item2, item3) to store the inputs and convert them into lowercase

item1 = input("Enter the first item you want to add to the cart: ").lower()
item2 = input("Enter the second item you want to add to the cart: ").lower()
item3 = input("Enter the third item you want to add to the cart: ").lower()
#We are using an if else statement to check if the item is in the list(available_items)
#If it is then add it by appending it to the shopping_cart list
#if the item is not available print out the message on the else statement
if item1 in available_items:
    shopping_cart.append(item1)
    print(f"{item1} has been added to your cart.")
else:
    print(f"Sorry, {item1} is not available in store.")

if item2 in available_items:
    shopping_cart.append(item2)
    print(f"{item2} has been added to your cart.")
else:
    print(f"Sorry, {item2} is not available in store.")


if item3 in available_items:
    shopping_cart.append(item3)
    print(f"{item3} has been added to your cart.")
else:
    print(f"Sorry, {item3} is not available in store.")

#Checking special items and add them to discount
if 'lemon' in shopping_cart:
    print("LEMON IS ON SALE! DISCOUNT APPLIED")

#Display the results:
print("\n Your shopping cart contains the following items: ")
print(shopping_cart)



