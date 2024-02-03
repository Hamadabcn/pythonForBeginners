import math

# string data type

# literal assignment of values
first = "Hamada"
last = "Farahat"

#print(type(first))
#print(type(last)== str)
#print(isinstance(first, str))

# constructor function
#pizza = str("Margarita")
#print(type(pizza))
#print(type(pizza)== str)
#print(isinstance(pizza, str))

# concatenation function
fullname = first + " " + last
print(fullname)
fullname += "!"
print(fullname)

# casting a number to a string
decade = str(1990)
print(type(decade))
print(decade)

statement = "I like electronic music from the " + decade + "s."
print(statement)

# multiply lines
multiline = '''

Hey, how are you?                                  

I was just checking in.                          
                    All good?

'''
print(multiline)

# escaping special characters
sentence = 'I\'m back at work!\they!\n\nWhere\'s this at\\located?\n'
print(sentence)

# string methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                                    "
multiline = "                        " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# build a menu
title = "menu".upper()
print(title.center(20, "=")) 

print("AmericanCoffee".ljust(16,".") +"1€".rjust(4))
print("Coffee With Milk".ljust(16,".") + "2€".rjust(4))
print("Tea".ljust(16,".") +"1€".rjust(4))
print("cheesecake".ljust(16,".") +"4€".rjust(4))
print("Coca Cola".ljust(16,".") +"2€".rjust(4))
print("Muffin".ljust(16,".") +"3€".rjust(4))
print("Pizza Margarita".ljust(16,".") +"8€".rjust(4))

print("")

# string index values
print(first[0])
print(first[1])
print(first[2])
print(first[3])
print(first[4])
print(first[5])
print(first[0:-1])
print(first[0:])

# some methods return boolean data
print(first.startswith("H"))
print(first.endswith("a"))

# boolean data type
myvalue =  True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# numeric data types

# integer data types
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# complex data types
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))

# casting a string to a number type
zipcode = "08036"
zip_value = int(zipcode)
print(type(zip_value))

# error if you attempt to cast incorrect data type
# zip_value = int("Barcelona")

