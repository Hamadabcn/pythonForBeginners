# while loop in python
value = 1
# while value <= 20:
#    print(value)
#    if value == 7: #to stop the loop at a point in this case 7
#        break
#    value += 1

#while value <= 10:
#        value += 1
#        if value == 4: #to stop the loop at a point
#            continue
#        print(value)
#else:
#        print("value no is equal to " + str(value))

# for loop in python
names = ["hamada", "amira", "yassin", "frida"]
#for _ in names: # her you can put any letter or symbol in this case _
#    print(_)
    
#for _ in "mississippi":
#    print(_)

#for x in names:
#    if x == "amira":
#        break
#    print(x)
    
#for x in names:
#    if x == "sara":
#        continue
#    print(x)

#for x in range(4):
#    print(x)
    
#for x in range(2, 4):
#    print(x)

#for x in range(5, 101, 10):
#    print(x)
#else:
#    print("glad that\'s over😁")    

names = ["hamada", "amira", "yassin", "frida"]
actions = ["codes", "eats", "sleeps", "repeats"]   

#for name in names: # the computer runs names first
#    for action in actions:
#        print(name + ", " + action + "😎" + ".") # concatenate 

for action in actions: # the computer runs actions first
    for name in names:
        print(name + ", " + action + "😎" + ".") # concatenate 
    