guests = ['Nelson Mandela', 'Rihanna', 'Elon Musk']

print("Great news! We found a bigger dinner table!\n")

# Add guests
guests.insert(0, 'Trevor Noah') # beginning
guests.insert(3, 'Thuso Mbedu') # middle
guests.append('Siya Kolisi') # end

# New invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner at my place on Friday.")