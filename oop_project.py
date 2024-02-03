from bank_account import *

Hamada = BankAccount(1000, 'Hamada')
Amira = BankAccount(2000, 'Amira')

#Hamada.getBalance()
#Amira.getBalance()

Hamada.deposit(500)

#Amira.withdraw(2500)
#Amira.withdraw(1000)

#Hamada.transfer(2500, Amira)
#Hamada.transfer(500, Amira)

#Hamada.transfer(100, Amira)

yassin = InterestRewardsAccount(1000, "Yassin")
yassin.getBalance()
yassin.deposit(100)
yassin.transfer(100, Hamada)

frida = SavingsAcct(1000, "Frida")
frida.getBalance()
frida.deposit(100)
frida.transfer(1000, yassin)