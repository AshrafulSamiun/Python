
print("Welcome to Calclutor Project")
print("1. Addition")
print("2. Subtriction")
print("3. Multiplication")
print("4. Division")
option=int(input("Select a Basic  Option for Calclutor Operation"))
if option==1:
    num1 = int(input("Enter First number"))
    num2 = int(input("Enter Second number"))
    sum=num1+num2
    print(" Addition is: "+str(sum))
elif option==2:
    num1 = int(input("Enter First number"))
    num2 = int(input("Enter Second number"))
    sub=num1-num2
    print(" Subtraction is: "+str(sub))
elif option==3:
    num1 = int(input("Enter First number"))
    num2 = int(input("Enter Second number"))
    mul=num1*num2
    print("Multiplication is: "+str(mul))
elif option==4:
    num1 = int(input("Enter First number"))
    num2 = int(input("Enter Second number"))
    div=num1/num2
    print("Division is: "+str(div))
else:
    print("Invalid Operation")