print("\nThis is called a Break Statement: break\n")

print("\nThis is a List: \n")

list = [5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5]

print(list)

sum = 0
for element in list:
    if element <= 0:
        break           #This is how WE use the break statement
    sum += element      #And this break statement means that 
                        #if element in the list is smaller than or equal to 0, we will break out of the code

print("\nWe Broke out of the code \n\n This is the sum of the positive numbers of the list: " + str(sum))