users = ['Hamada', 'Amira', 'Yassin', 'Frida']

data = ['Hamada', 42, True]

emptylist = []

print("Hamada" in data)

print(users[2])
print(users[-1])

print(users.index('Frida'))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))

users.append('Mahmoud')
print(users)


users += ['Amr', 'Noha', 'Talia', 'Kensi', 'Rami', 'Zizi', 'Riri', 'Mami', 'Nuran', 'Omar', 'Nahal', 'Salama', 'Sherif', 'Bido']
print(users)

users.extend(['Mahmoud', 'Walla', 'Gana', 'Adam', 'Younes'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Hamed', 'Salah']
print(users)

users[1:3] = ['Magda', 'Hoda']
print(users)

users.remove('Salah')
print(users)

# pop method to delete the last item from a list
print(users.pop())
print(users)

# del to delete a specific user
del users[0]
print(users)

# data.clear to delete the whole list
# del data 
data.clear()
print(data)

# to sort the users in alphabetical order
users[1:2] = ['hamada']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Niel", True])
print(mylist)

# tuples
mytuple = tuple(('Hamada', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
mylist.append('Niel')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))

