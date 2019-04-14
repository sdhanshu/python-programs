print("\nSum of all the numbers till 5 using a While loop: \n")

# This is called a While loop: 

total = 0
x = 1
while x < 5:
    total += x
    x += 1

print(total)

print("\nThis is a List: \n")

list = [5, 3, 6, 2, 1, -1, -2, -8, -9]

print(list)

print("\nSum of all the positive numbers in the list: \n")

sum = 1
i = 0
while list[i] > 0:
    sum += list[i]
    i += 1

print(sum)