#Creating a list of animals with the variable called animals
animals = ['dog', 'cat', 'cow', 'fish', 'tiger', 'fox']

#Creating a for loop that will print each item one by one
#Inside the loop we are getting each items length
#And printing out a sentence with a title()
for animal in animals:
    length = len(animal)
    print(f"My animal is a {animal.title()} and it has {length} letters")

#Avoid doing this
for animal in animals:
    length = len(animal)
print(f"My animal is a {animal.title()} and it has {length} letters")