
#which is largest of three numbers

num1 = int(input("Enter the number 1 :"))
num2 = int(input("Enter the number 2 :"))
num3 = int(input("Enter the number 3 :"))

if (num1 > num2 and num1 > num3):
    print(num1,"is largest number")
elif(num2 > num3):
    print(num2,"is largest number")
else:
    print(num3,"is largest number")



