import random
import os

def factors(number):
    fs = []
    for i in range(1,number):
        if number % i:
            fs.append(i)
    return fs

while 1:
    os.system("clear")
    numbers = factors(random.randint(1,20))

    x1 = random.choice(numbers)
    x2 = random.choice(numbers)

    print("x^2+" + str(x1+x2) + "x+" + str(x1*x2))

    num1 = input("Factor 1: ")
    num2 = input("Factor 2: ")

    if (int(num1) == x1 and int(num2) == x2) or (int(num1) == x2 and int(num2) == x1):
        print("correct")
    else:
        print("incorrect. The correct answer would be ")

    print("(x+" + str(x1) + ") (x+" + str(x2) + ")")
    input("")
