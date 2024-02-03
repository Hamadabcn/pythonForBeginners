import os

# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if doesn't exist

f = open("names.txt", "r")
# print (f.read())
# print (f.read(6))

# print(f.readline())
# print(f.readline())

for line in f:
    print(line)

f.close()

try:
    f = open("names.txt", "r")
    print(f.read())
except:
    print("The file does not exist.")
finally:
    f.close()
    
# Append - creates the file if it doesn't already exist
f = open("names.txt", "a")
f.write("Tom\n")
f.close() 

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrites)
f = open("context.txt", "w")
f.write("I deleted all of the context\n")
f.close()

f = open("context.txt")
print(f.read())
f.close()

# Two ways to create a new file

# opens a file for writing, it also creates a file if it doesn't exist
f = open("names_list.txt", "w")
f.close()

# creates the specified file, but returns an error if the file exists
if not os.path.exists("Hamada.txt"):
    f = open("Hamada.txt", "x")
    f.close()
    
# Delete a file
# avoid an error if it doesn't exist
if os.path.exists("Hamada.txt"):
    os.remove("Hamada.txt")
else:
    print("The file you want to delete doesn't exist")
    
with open("more_names.txt") as f:
    content = f.read()
    
with open("names.txt", "w") as f:
    f.write(content)