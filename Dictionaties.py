# A dictionary is like a look up table in python

d = {}          # We can make an empty dictionary by doing this

# d = {"Ram" = 24, "Shyam" = 32}

d["Ram"] = 24   # This says add a new key Ram which has value 24
d["Shyam"] = 32 # This says add a new key Shyam which has value 32
d["Geeta"] = 16 # This says add a new key Geeta which has value 16

print("\nThe value of the key Ram is : ")
print(d["Ram"])
print("The value of the key Shyam is : ")
print(d["Shyam"])
print("The value of the key Geeta is : ")
print(d["Geeta"])

d["Geeta"] = 20 # We can change the value of any key in the dictionary like this

print("Now the value of the key Geeta is : ")
print(d["Geeta"])

# Most commonly keys are strings and numbers

d[1] = 100     # This says add a new key '1' which has value 100

print("The value of the key 1 is : ")
print(d[1])
print("\n")

# How to iterate over key-value pairs ?

print("All the Keys in the dictionary are : \n")

for key, value in d.items():
    print("Key:")
    print(key)
    print("Value:")
    print(value)
    print("")