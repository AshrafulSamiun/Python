


class BankAccount:

    balance=0
    name=""

    def __init__(self,user_name,initial_balance):
        self.name=user_name
        self.balance=initial_balance
        self.minimum_balance=500

    def Diposlit(self,amount):
        if amount>0:
            self.balance+=amount
            return amount
        else:
            print("Invalid Amount")

    def Withdraw(self,amount):
        if amount>0 and (amount+self.minimum_balance)<=self.balance:
            self.balance-=amount
            return amount
        else:
            return f"Insuffecient Banance"

    def CheckBalance(self):
        return self.balance


print("Welcome to ABC Banking System")
user_name=input("Enter User/Account Name")
initial_balance=float(input("Initial Balance"))
account=BankAccount(user_name,initial_balance)
print(f"Account Name: {account.name}")
print(f"Initial Balance : {account.balance}")
print("Enter 0 for Exit")
print("Enter 1 for Deposit")
print("Enter 2 for Withdraw")
while True:
    option=int(input("What do want to do"))
    if option==0:
        print("Thanks for using our service")
        break
    elif option==1:
        deposit_amount = float(input("Enter Deposit Amount"))
        print(f"Deposit Balance : {account.Diposlit(deposit_amount)}")
        print(f"After Deposit , Your  Balance is : {account.CheckBalance()}")
    elif option==2:
        withdraw_amount = float(input("Enter Withdraw Amount"))
        print(f"Withdraw Balance : {account.Withdraw(withdraw_amount)}")
        print(f"After Withdraw , Your  Balance is : {account.CheckBalance()}")
    else:
        print("Invalid Operation")







