name = "hamada"
count = 2 * 2

def another():
    color = "blue"
    global count 
    count += 5
    print(count)
    
    def greeting(name):
        #nonlocal color
        color = "red"
        print(color)
        print(name)
    greeting("hamada")

another()
