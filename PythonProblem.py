a = ['Mango', 'Apple', 'Banana', 'Watermelon']

print("\nThis is the list: " + str(a))

print("\nQ: Can you print the first element of a list once and then the second one twice and so on ?")

print("\nThis is the solution to the problem: \n")

for element in range(len(a)):
    for i in range(element + 1):
        print(a[element])
        #element = 0 -> i = 0
        #element = 1 -> 1 = 0, 1
        #element = 2 -> i = 0, 1, 2
        #element = 3 -> i = 0, 1, 2, 3