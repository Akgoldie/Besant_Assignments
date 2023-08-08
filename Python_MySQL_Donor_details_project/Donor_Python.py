from tabulate import tabulate
import mysql.connector

connect = mysql.connector.connect(host="localhost", user="root", password="root", database="Ajkbloodbank")

"""
#to check if connected or not connected 
if connect:
    print("connected")
else:
    print("Not connected")

"""


def insert(DONER_NAME, AGE, GENDER, ADDRESS, DISTRICT, PHONE_NUMBER, EMAIL_ID):
    # print("insert")
    res = connect.cursor()
    sql = "insert into Donor_reg (DONER_NAME,AGE,GENDER,ADDRESS,DISTRICT,PHONE_NUMBER,EMAIL_ID ) values (%s,%s,%s,%s,%s,%s,%s)"
    Donor = (DONER_NAME, AGE, GENDER, ADDRESS, DISTRICT, PHONE_NUMBER, EMAIL_ID)
    res.execute(sql, Donor)
    connect.commit()
    print("Successfully insert the data")


def update(DONER_NAME, AGE, GENDER, ADDRESS, DISTRICT, PHONE_NUMBER, EMAIL_ID, ID):
    # print("update")
    res = connect.cursor()
    sql = "update Donor_reg set DONER_NAME=%s ,AGE=%s ,GENDER=%s ,ADDRESS=%s ,DISTRICT=%s ,PHONE_NUMBER=%s ,EMAIL_ID=%s where ID=%s "
    Donor = (DONER_NAME, AGE, GENDER, ADDRESS, DISTRICT, PHONE_NUMBER, EMAIL_ID, ID)
    res.execute(sql, Donor)
    connect.commit()
    print("Successfully update the data")


def delete(ID):
    # print("delete")
    res = connect.cursor()
    sql = "delete from Donor_reg where ID=%s "
    Donor = (ID,)
    res.execute(sql, Donor)
    connect.commit()
    print("Successfully delete the data")


def preview():
    # print("preview")
    res = connect.cursor()
    sql = "SELECT ID,DONER_NAME,AGE,GENDER,ADDRESS,DISTRICT,PHONE_NUMBER,EMAIL_ID from Donor_reg"
    res.execute(sql)
    # result=res.fetchone()  first data
    # result = res.fetchmany()  particular data mention within brackets
    result = res.fetchall()
    print(tabulate(result,
                   headers=["ID", "DONER_NAME", "AGE", "GENDER", "ADDRESS", "DISTRICT", "PHONE_NUMBER", "EMAIL_ID"]))


"""
print("1. INSERT DATA")
print("2. UPDATE DATA")
print("3. DELETE DATA")
print("4. PREVIEW DATA")
print("5. QUIT")

"""
while True:

    print("1. INSERT DATA")
    print("2. UPDATE DATA")
    print("3. DELETE DATA")
    print("4. PREVIEW DATA")
    print("5. QUIT")

    choice = int(input("\n Enter your choice: "))

    if (choice == 1):
        DONER_NAME = input("Enter the DONER_NAME: ")
        AGE = int(input("Enter the AGE: "))
        GENDER = input("Enter the GENDER: ")
        ADDRESS = input("Enter the ADDRESS: ")
        DISTRICT = input("Enter the DISTRICT: ")
        PHONE_NUMBER = input("Enter the PHONE_NUMBER: ")
        EMAIL_ID = input("Enter the EMAIL_ID: ")
        insert(DONER_NAME, AGE, GENDER, ADDRESS, DISTRICT, PHONE_NUMBER, EMAIL_ID)

    elif (choice == 2):
        ID = int(input("Enter the Id to update: "))
        DONER_NAME = input("Update the DONER_NAME: ")
        AGE = int(input("Update the AGE: "))
        GENDER = input("Update the GENDER: ")
        ADDRESS = input("Update the ADDRESS: ")
        DISTRICT = input("Update the DISTRICT: ")
        PHONE_NUMBER = input("Update the PHONE_NUMBER: ")
        EMAIL_ID = input("Update the EMAIL_ID: ")
        update(DONER_NAME, AGE, GENDER, ADDRESS, DISTRICT, PHONE_NUMBER, EMAIL_ID, ID)

    elif (choice == 3):
        ID = int(input("Enter the Id to delete: "))
        delete(ID)

    elif (choice == 4):
        preview()

    elif (choice == 5):
        print("Thank You")
        break

    else:
        print("Invaild choice, please try again ")



