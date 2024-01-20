#Simple Calculator
#Lam Manning
#Nov. 29 2023

#Intial

#Func
#Takes two numbers, adds them, and returns the result
#num1 is an integer
#num2 is an interger
def addition(num1, num2):
    total = num1 + num2
    return total
#Takes two numbers, Subtracts Num2 from Num1, and prints difference out
#num1 is an integer
#num2 is an interger
def subtraction(num1, num2):
    difference = num1 - num2
    return difference
#Takes two numbers, Multiplies them, and prints product out
#num1 is an integer
#num2 is an interger
def multiplication(num1, num2):
    product = num1*num2
    return product
#Takes two numbers, Divides num1 by num2, and prints quotient out
#num1 is an integer
#num2 is an interger
def division(num1, num2):
    if(num2==0):
        print("Error! Can Not Divide by 0")
    else:
        quotient = num1/num2
        return quotient
#Takes two numbers, Divides num1 by num2, and prints remainder out
#num1 is an integer
#num2 is an interger
def mod(num1, num2):
    if(num2==0):
        print("Error! Can Not Divide by 0")
    else:
        remainder = num1 % num2
        return remainder
def exponent(num1, num2):
    product = num1 ** num2
    return product
#Prints a goodbye message  
def quit():
    print("Goodbye!")
#Runs the calculator and all it's operations
#Operation: Integer
#num1: Integer
#num2:Integer
def calculator():
    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Mod \n6.Exponent \n7. Quit Program")
    operation = int(input("Option: "))
    num1 = float(input("What is the first number: "))
    num2 = float(input("What is the second number: "))

    if(operation==1):
       print(addition(num1, num2))
    elif(operation==2):
        print(subtraction(num1, num2))
    elif(operation==3):
        print(multiplication(num1, num2))
    elif(operation==4):
        print(division(num1, num2))
    elif(operation==5):
        print(mod(num1, num2))
    elif(operation==6):
        print(exponent(num1, num2))
    elif(operation==7):
        quit()
    else:
        print("Please type a number from 1-6")
        calculator()
#Asks if user wants to use the calculator again
#val: string
def again():
    val = input("Do you wish to do another operation? (Yes or No): ")
    if (val=="Yes"):
        calculator()
        again()
    elif(val=="No"):
        quit()
    else:
        print("Please type Yes or No.")
        again()
#Main
print("Welcome to Simple Calculator")
print("Please choose an opperation: (Type in a number between 1-6)")
calculator()
again()
