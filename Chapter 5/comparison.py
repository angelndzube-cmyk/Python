# creating two variables called a and b
# we are checking if the values are equal to each other by using the equal to operator(==)
a = 15
b = 12
print("1. is equal to b: ", a == b)


# checking if a is not equal to b
print("2. is not equal to b:", a != b)

#checking if 2 condition are true or false using the AND operator
c = 11
d = 20
print("3. are the following conditions true or false: ", c < 15 and d > 18)

#checking if 2 condition are true or false using the OR operator
print("4. are the following conditions true or false: ", c > 15 and d > 18)


#we are checking if a value is in the list using NOT IN
numbers = [2,4,6,8,10]
print("5. is the number 3 not in the numbers list: ", 3 not in numbers)

#we are checking if a value is in the list using IN
print("6. is the number 3 in the numbers list: ", 3 in numbers)

#BOOLEAN - meaning the output is either true or false
is_Sunny = True
is_Cold = False
print("7. is the boolean expression true or false using AND operator: ", is_Sunny and is_Cold)

#Using OR operator
print("7. is the boolean expression true or false using OR operator: ", is_Sunny or is_Cold)