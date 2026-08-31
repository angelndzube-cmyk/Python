# 7-4. Pizza Toppings
prompt = "Enter a pizza topping (type 'quit' to finish): "

while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza!")