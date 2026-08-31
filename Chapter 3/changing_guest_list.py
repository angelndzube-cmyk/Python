guests =['Nelson Mandela','Beyonce','Elon Musk']
# first set of invites
for guest in guests:
    print (f"dear {guest},you are invited to dinner at my place on friday.")
print () 
print (f"Unfortunately,{guests[1]} cant make it to dinner.")   
# replace the guest who cant come
guests[1] ='Rihanna'
# second sets of invites
print("\nNew invitations:")
for guest in guests :
    print(f"Dear {guest}, you are invited to dinner at my place on Friday.")