import math

# Addition
def addition(num1,num2):
    return num1+num2

# Subtraction
def Subtraction(num1,num2):
     return num1-num2
# Division
def division(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1/n2


# Multiplication
def multiply(num1,num2):
    return num1 * num2
  
# exponential
def exponential(num1,num2):
    return num1 ** num2

# Square
def square(num1,num2):
    print("The square of num1" ,num1 ** 2)
    print("The square of num2" ,num2 ** 2)
# Squreroot
def squareroot(num1,num2):
    if num1 >= 0:
        print("Square root of first number:", math.sqrt(num1))
    else:
        print("Square root of first number: Not defined for negative numbers")

    if num2 >= 0:
        print("Square root of second number:", math.sqrt(num2))
    else:
        print("Square root of second number: Not defined for negative numbers")

#  factorial
def factorial(num1,num2):
    if num1 >= 0:
        print("Factorial of num1:", math.factorial(num1))
    else:
        print("Factorial of num1: Not defined for negative numbers.")

    if num2 >= 0:
        print("Factorial of num2:", math.factorial(num2))
    else:
        print("Factorial of num2: Not defined for negative numbers.")



def main():
    cont=1
    while cont==1 :
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

        print("\nChoose operation:")
        print("+  : Addition")
        print("-  : Subtraction")
        print("/  : Division")
        print("*  : Multiplication")
        print("^  : Exponential (num1 ^ num2)")
        print("sq : Square of numbers")
        print("sr : Square root of numbers")
        print("!  : Factorial of numbers")
        choice = input("\nEnter operator: ")
        if choice == "+":
            print("Result:", addition(num1, num2))
        elif choice == "-":
            print("Result:", Subtraction(num1, num2))
        elif choice == "/":
            print("Result:", division(num1, num2))
        elif choice == "*":
            print("Result:", multiply(num1, num2))
        elif choice == "^":
            print("Result:", exponential(num1, num2))
        elif choice == "sq":
            print("Result:", square(num1,num2))
        elif choice == "sr":
            squareroot(num1, num2)
        elif choice == "!":
            factorial(num1, num2)
        else:
            print("Invalid operator!")
        cont=int(input("Continue? 1 - yes, 0 - no"))

if __name__ == "__main__":
    main()