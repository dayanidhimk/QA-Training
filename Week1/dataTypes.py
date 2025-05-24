def sumOfNumbers(num1,num2):
    n1 = int(num1)
    n2 = int(num2)
    return (n1 + n2)


def printSum():
    print("Enter two numbers:")
    num1 = input()
    num2 = input()
    print("Sum of the numbers =",sumOfNumbers(num1,num2))

printSum()