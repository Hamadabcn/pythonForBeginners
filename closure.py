# closure is a function having access to the scope to its parents
# function after parents function has returned.

def parent_function(person, coins):
    #coins = 3
    
    def play_game():
        nonlocal coins
        coins -=1
        
        if coins > 1:
            # The line `print("\n" + person  + " has " + str(coins) + " coins left. ")` is printing a
            # message to the console. The message includes the value of the variable `person`, the
            # value of the variable `coins`, and some additional text. The purpose of this line is to
            # display the number of coins the person has left.
            print("\n" + person  + " has " + str(coins) + " coins left💰. ")
        elif coins == 1:
            print("\n" + person  + " has " + str(coins) + " coin left💰. ")
        else:
            print("\n" + person  + " is out of coins😯. ")
            
    return play_game

yassin = parent_function("Yassin", 3)
frida = parent_function("Frida", 5)

yassin()
yassin()

frida()
frida()

yassin()
frida()

frida()
frida()
