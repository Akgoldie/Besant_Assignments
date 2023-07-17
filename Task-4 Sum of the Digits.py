num=int(input("Enter the number:"))
sum=0
temp=num

while(temp!=0):
    digit=temp%10
    sum=sum+digit
    #print("sum:",sum)
    temp=temp//10
    #print("temp:", temp)



print("Sum of digits:",sum)

