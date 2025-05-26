def divide(a,b):
    answer = 0
    try:
        answer = a/b
    except ZeroDivisionError:
        print("Math error! Can't divide a number by zero...")
    else:
        print("Answer =", answer)

print("When we divide 4/0 ...\n")
divide(4,0)