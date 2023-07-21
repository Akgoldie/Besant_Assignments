# calculator

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("if you want to sum type 1")
print("if you want to subtract type 2")
print("if you want to multiply type 3")
print("if you want to divide type 4")
print("if you want to modulo type 5")
print("if you want to floor division type 6")
print("if you want to exponent type 7")

#print("if you want to break type 0")
while(1==1):

    operators = int(input())

    if operators == 1:
        print(num1, "+", num2, "=", num1 + num2)
        print("if you want to break type 0")
    elif operators == 2:
        print(num1, "-", num2, "=", num1 - num2)
        print("if you want to break type 0")
    elif operators == 3:
        print(num1, "*", num2, "=", num1 * num2)
        print("if you want to break type 0")
    elif operators == 4:
        print(num1, "/", num2, "=", num1 / num2)
        print("if you want to break type 0")
    elif operators == 5:
        print(num1, "%", num2, "=", num1 % num2)
        print("if you want to break type 0")
    elif operators == 6:
        print(num1, "//", num2, "=", num1 // num2)
        print("if you want to break type 0")
    elif operators == 7:
        print(num1, "**", num2, "=", num1 ** num2)
        print("if you want to break type 0")
    elif operators == 0:
        break

    else:
        print("Error invalid numbers or function")
