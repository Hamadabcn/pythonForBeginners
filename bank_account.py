class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName,):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = €{self.balance:.2f}")
        
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = €{self.balance:.2f}")
        
    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete.")
        self.getBalance()
        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of €{self.balance:.2f}")
            
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw completed successfully.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted, sorry for the inconvenience: {error}\n")
            
    def transfer(self, amount, account):
        try:
            print("\n********************\n\nStarting to transfer. . .🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer completed! ✅\n\n********************")
            
        except BalanceException as error:
            print(f"\nTransfer interrupted, sorry for the inconvenience ❌ {error}\n")
            
class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit completed.")
        self.getBalance()
        
class SavingsAcct(InterestRewardsAccount):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5
        
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted, sorry for the inconvenience: {error}\n")