num=int(input("Enter the number:"))
count=0
temp=num

while(temp!=0):
    count=count+1
    temp=temp//10
    #print("temp:", temp)

print("Count of digits:",count)