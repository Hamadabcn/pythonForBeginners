squared = lambda num : num * num
# def squared(num): return num * num (another way of doing the same thing)

print(squared(9))

addTwo = lambda num : num + 2
# def addTwo(num): return num + 2 (another way of doing the same thing)

print(addTwo(4))

sum_total = lambda a, b : a + b
# def sum(a, b): return a + b (another way of doing the same thing)

print(sum_total(20, 22))

#################################

def funcBuilder(x):
    return lambda num : num + x

addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

print(addTen(7))
print(addTwenty(7))

#################################

numbers = [1, 2, 3, 6, 7, 9, 10, 11, 12, 15, 18, 20, 21, 23, 27, 30, 36, 41, 45]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

#################################

odd_nums = filter(lambda num: num % 2 != 0, numbers)

print(list(odd_nums))

#################################

from functools import reduce

numbers = [1, 2, 3, 4, 5, 1]

total = reduce(lambda acc, curr : acc + curr, numbers, 10)

print(total)

print(sum(numbers, 10))


names = ['Mohamed Farahat', 'Amira Abdalla', 'Yassin Mohamad', 'Frida Mohamad']

char_count = reduce(lambda acc, curr : acc + len(curr), names, 0)

print(char_count)

