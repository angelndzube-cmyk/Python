guests = ['Trevor Noah', 'Nelson Mandela', 'Rihanna', 'Thuso Mbedu', 'Elon Musk', 'Siya Kolisi']

print("The new table won't arrive in time. I can only invite 2 people for dinner.\n")

# Remove guests until only 2 remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

print("\nThe 2 people still invited:")
for guest in guests:
    print(f"Dear {guest}, you're still invited to dinner!")

# Empty the list
del guests[0]
del guests[0]

print("\nFinal guest list:", guests) # []