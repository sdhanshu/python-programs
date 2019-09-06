print("\nThis is the List :\n")

a = ["banana", "grapes", "mango"]

print(a[0])
print(a[1])      # This is a lot of work
print(a[2])

print("\nThis is the List with a for loop: \n")
    
for element in a :     # This means for each element of list a
    print(element)     # do the following, which is printing list a
                       # Also in this loop, element is something we can choose
                       # We can name it anything 

# If you want to add the elements of a list using for loop

print("\nThis is the second List : \n")

b = [70, -100 , 80]

print(b)

total = 0

for element in b:
    total += element



print("\nThe Sum is " + str(total) +" \n") 

# If we want to do a sum till a large number

print("This is the third list using range:  \n")

c = list(range(1, 51))

print(c)

sum = 0

for element in c:
    sum += element     # Shortcut of sum = sum + element

print("\nSum of this list is: " + str(sum) + "\n")

# What if you want to add multiples of a specific number like 3

print("This is the fourth list using range: \n")

d = list(range(1, 7))

print(d)

sum2 = 0

for element in d:
    if element % 3 == 0:
        sum2 += element

print("\nSum of multiples of 3 in this list is: " + str(sum2) + "\n")