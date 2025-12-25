#Create Account class with 2 attributes - balance & account no.
#Create methods for debit, credit & printing the balance.

class Account:

    def __init__(self,balance,accountNo):
        self.balance = balance
        self.accountNo = accountNo

    def debit(self,dAmmount):
        self.balance -=dAmmount
        print("RS.",dAmmount,"was Debited...!")
        print("Total Account Balance",self.printingBal())

    def credit(self,cAmmount):
        self.balance += cAmmount
        print("Rs.",cAmmount,"Was Credited...!")
        print("Total Account Balance",self.printingBal())

    def printingBal(self):
        return self.balance


account = Account(10000,123456)
account.debit(500)  
account.credit(1115)      
account.credit(500)   
account.printingBal()