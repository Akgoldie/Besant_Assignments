# Given character is uppercase OR lowercase

letter=input("Enter the letter :")

if(letter>='a' and letter<='z'):
    print("This character is lower case")
elif(letter>='A' and letter<='Z'):
    print("This character is upper case")
else:
    print("Invalid character")


