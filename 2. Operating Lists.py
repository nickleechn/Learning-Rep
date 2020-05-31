#print("Hello, world.")

friends = ['kiki', 'layla', 'kawahi', 'huskar'] # List of friends
print(friends)
moved_out = 'huskar' #Define Huskar as the one who moved out
friends.remove(moved_out) #Remove Huskar from the friend list
print(friends)
print(f"\nThe friend who left us is {moved_out.title()}.")

friends_again = [] #Creating an empty list
friends_again.append('nick') #Add Nick
friends_again.append('kiki') #Add Kiki
print(friends_again)
removed = friends_again.pop(0) #Remove Nick from the List and define him as "removed"
print(friends_again)
print(f"\nThe guy who got removed was {removed.title()}")

#This secion shows how to sort a list
nancarrow = ['nick', 'kiki', 'kawahi', 'layla', 'huskar']
nancarrow.sort(reverse=True) #Sort the list in reverse-alphabetic order
print(nancarrow)
print(sorted(nancarrow)) #Display the list alphabetically, but not permanantly