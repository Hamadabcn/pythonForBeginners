def hello_world():
    print("\nhello world!\n")
    
hello_world()

# adding parameters
def sum(num1, num2):
    if(type(num1) is not int or type(num2) is not int):
        return
    return num1 + num2

total = sum(2, 3) , sum(2, 4)
print(total)
    
def multiple_items(*args):
    print(args)
    print(type(args))
    print(len(args))
    print(bool(args))
    print(str(args))
    
multiple_items("hamada", "amira", "yassin", "frida")

def mult_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))
    print(len(kwargs))
    print(bool(kwargs))
    print(str(kwargs))

mult_named_items(first = "hamada", last = "amira")