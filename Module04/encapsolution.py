class BankAccount:
    __balance=0
    #Deposit
    def Diposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print("Deposit Succefully")
        else:
            print("invalid operation")

    #Widraw
    def Widraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print("Withdraw Succefully")
        else:
            print("Insufficent Balance")

    #Check Balance
    def CheckBalance(self):
        return self.__balance


obj=BankAccount()
obj.Diposit(5001)
print(obj.CheckBalance())
obj.Widraw(21000)
print(obj.CheckBalance())