# Using range and for loop to print each item in the list one by one
for number in range(7):
    print(number)

# Using list() and range() to get the even numbers
# We start at 0 and stop at 11 but excluding 11
# We add 2 to every count e.g (0+2 = 2 / 2+2 = 4 / 4+2 = 6)
even_numbers = list(range(0,11,2))
print(even_numbers)

# Odd numbers
# We start at 1 and stop at 12 but excluding 12
# We add 2 to every count

# We start at 0 and stop at 11 but excluding 11
# We add 2 to every count e.g (0+2 = 2 / 2+2 = 4 / 4+2 = 6)
even_numbers = list(range(0,11,2))
print(even_numbers)

# Odd numbers
# We start at 1 and stop at 12 but excluding 12
# We add 2 to every count e.g (1+2 = 3 / 3+2 = 5 / 5+2 = 7)
odd_numbers = list(range(1,12,2))
print(odd_numbers)

# Using the square root
# Starting with an empty array to store the final results
# We calculate at 1 and stop at 4 but excluding 4
squares = []
for number in range(1,4):
    square = number ** 2  # (1 **2 = 1)
    squares.append(square)
print(squares)

#Min(), Max(), Sum()
numbers = [2, 5, 1, 15, 25, 50,46, 72]

print("Min: ", min(numbers))
print("Max: ", max(numbers))
print("Sum: ", sum(numbers))

#List Comprehensions