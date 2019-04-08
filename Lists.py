print("\nThis is the first list: \n")

a = [1, 2, 3, 4, 5]      # The items in the square Brackets forms a LIST

print(a)

print("\nThis is the second list: \n")

a.append(-1)              # Append means to add an item to the list

print(a)

print("\nThis is the third list : \n")

a.append("mango, banana")# We can append anything to a list 

print(a)

print("\nThis is the fourth list: \n")

a.pop()                   # We use .pop remove the last item from the list

print(a)

print("\nThis is the first item of the list: \n")

print(a[0])                      # When we have to retrieve an item from the list, 
                                 # We use its INDEX number to do so
                                 # Index numbers starts at 0

print("\nThis is the second item of the list: \n")

print(a[1])

print("\nThis is the fifth list: \n")

a[5] = "grapes"                   # We can also change the items of the list by assigning them a value

print(a)

print("\nThis is the sixth list: \n")

a[0], a[5] = a[5], a[0]           # We can swap the items of the list by writing this piece of code

print(a)