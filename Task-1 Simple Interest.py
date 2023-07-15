#calculate the simple interest

principle = int(input("Enter your principal amount :"))
interest = int(input("Enter your interest :"))
no_of_years = int(input("Enter the No of years :"))

SI = (principle*interest*no_of_years)/100
print("Simple Interest :",SI)

Amount = principle+SI
print("Total Amount is :",Amount)
