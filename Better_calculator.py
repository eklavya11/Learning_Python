#Better_calculator

op = int(input("Choose the type of calculation:\n1. Enter 1 for addition\n2. Enter 2 for substraction\n3. Enter 3 for multiplication\n4. Enter 4 for division\nEnter here:"))
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))

if(op==1):
    print("The sum of "+str(num1)+" & "+str(num2)+" is "+str(num1+num2))
elif(op==2):
    print("The difference of "+str(num1)+" & "+str(num2)+" is "+str(num1-num2))
elif(op==3):
    print("The multiplication of "+str(num1)+" & "+str(num2)+" is "+str(num1*num2))
elif(op==4):
    print("The division of "+str(num1)+" & "+str(num2)+" is "+str(num1/num2))
else:
    print("Please input correct option.")
