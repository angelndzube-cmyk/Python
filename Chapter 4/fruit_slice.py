#Creating a list of fruits with a variable named fruits
fruits = ["banana", "peach", "berry", "guava", "lemon", "mango"]

#Slicing: starting the slice with an empty value which means start at the beginning
#stopping at 4 but excluding 4
#store the results in a variable called sliced_fruit
sliced_fruit = fruits[:4]

#printing out the results:
print("Result 1:")
for fruit in sliced_fruit:
    print(fruit)

#Making a copy of the entire fruits list in a new variable called copy_of_fruits_list
#copy_of_fruits_list = ["banana", "peach","berry", "guava", "lemon", "mango"]
copy_of_fruits_list = fruits[:]

#Adding a new fruit to the copy list
#copy_of_fruits_list = ["banana", "peach","berry", "guava", "lemon", "mango", "apple"]
copy_of_fruits_list.append("apple")