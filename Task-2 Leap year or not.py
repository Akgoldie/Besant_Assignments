# given year is leep year or not

year = int(input("enteŕ the year:"))

if (year % 400 == 0 and year % 100 == 0):
    print(year, "is leap year")

elif (year % 4 == 0 and year % 100 != 0):
    print(year, "is leap year")

else:
    print(year, "is not leap year")
