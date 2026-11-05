#Creating a list of fruits with a variable named fruits
fruits = ["banana", "peach", "berry", "guava", "lemon", "mango"]

#Slicing: starting the slice with an empty value which means start at the beginning
#stopping at 4 but excluding 4
#store the results in a variable called sliced_fruit
sliced_fruit = fruits[:4]

#Printing out the results:
print("Result 1")
for fruit in sliced_fruit:
    print(fruit)

    #Slicing: starting the slice 1
#stopping at 5 but excluding 5
#store the results in a variable called sliced_fruit
sliced_fruit = fruits[1:5]

#printing out the results:
print("Result 2:")
for fruit in sliced_fruit:
    print(fruit)

#Slicing: starting the slice 1
#do not have a stopping point which means it will print out everything after the start
#store the results in a variable called sliced_fruit
sliced_fruit = fruits[1:]

#printing out the results:
print("Result 3:")
for fruit in sliced_fruit:
    print(fruit)