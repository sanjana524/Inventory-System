#Vehicle Inventory System using Python and Mysql.
#This projectis for Car Dealersship that can add, remove and edit vehicles. 
import pymysql
import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

con = pymysql.connect("localhost","root","sm18","inventory")
cur=con.cursor()
def main():
    connection()
    
def connection():
    username="auto"
    password="mobile"
    print("Username : ")
    answer1=input()
    print("Password : ")
    answer2=input()
    if answer1==username and answer2==password:
        print("WELCOME TO VEHICLE INVETORY SYSTEM")
        inventory()
    else:
        print("Incorrect Username or Password, Please try again:")
        exit
    
def option():
    pass
    ch=input("Do you wish to continue with the menu,Press y for yes or n for no :")
    if(ch=='y' or ch=='Y'):
                   inventory()
    else:
                   exit
                   print("Thank You for being our valuable customer:")
                
    
def inventory():
    print("*INVENTORY MENU*")

    print()

    userinput = input("""
                      #1 Add Vehicle to Inventory
                      #2 Delete Vehicle from Inventory
                      #3 View Current Inventory
                      #4 Update Vehicle in Inventory
                      #5 Export Current Inventory
                      #6 Generate Bargraph
                      #7 Quit

                      Please choose from one of the above options: """)

    if   userinput == "1":
         addvehicles()
    elif userinput == "2":
         deleteinventory()
    elif userinput == "3":
         viewinventory()
    elif userinput=="4":
         updateinventory()
    elif userinput=="5":
         exportinventory()
    elif userinput=="6":
         bargraph()
    elif userinput=="7":
        print("Goodbye:")
        exit
    else:
        print("This is an invalid input")
        print("Please try again")
        inventory()

def addvehicles():
    id=int(input("Enter vehicle id :"))
    category=input("Enter vehicle category :")
    make=input("Enter vehicle make :")
    colour=input("Enter vehicle colour :")
    mileage=int(input("Enter vehicle mileage :"))
    year=input("Enter vehicle year :")
    values=(id,category,make,colour,mileage,year)
    cur=con.cursor()
    st="insert into vehicledata values(%s,%s,%s,%s,%s,%s)"
    result=cur.execute(st,values)
    con.commit()
    if(result==True):
        print("This vehicle has been added, Thank you")
        option()
    
def viewinventory():
    
    id=int(input("Enter vehicle id to view the data :"))
    st="select * from vehicledata where id in ( (%s),(%s))"
    cur=con.cursor()
    cur.execute(st,(id,id))
    data=cur.fetchall()
    print(data)
    option()

def updateinventory():
      
    print(" Update can be done on the following fields 1.Make, 2.Colour No, 3.Mileage")
    print("Enter option 1-3 for update :")
          
    ch=int(input())
    if(ch==1):
        id=int(input("Enter vehicle id to update the data :"))
        ch1=str(input("Enter the new make :"))
        values=(ch1,id)
        st="update vehicledata set make=%s where id=%s"
        cur=con.cursor()
        data=cur.execute(st,values)
        con.commit()
        if(data==True):
            print("Vehicle Make updated successfully ")
        else:
            print("Error try again :")
            print(data)
    elif(ch==2):
        id=int(input("Enter vehicle id to update the data :"))
        ch1=input("Enter the new colour :")
        values=(ch1,id)
        st="update vehicledata set colour=%s where id=%s"
        cur=con.cursor()
        data=cur.execute(st,values)
        con.commit()
        if(data==True):
            print("Vehicle colour updated successfully ")
        else:
            print("Error try again :")
    elif(ch==3):
        id=int(input("Enter Vehicle id to update the data :"))
        ch1=input("Enter the new mileage :")
        values=(ch1,id)
        st="update vehicledata set mileage=%s where id=%s"
        cur=con.cursor()
        data=cur.execute(st,values)
        con.commit()
        if(data==True):
            print("Vehicle mileage updated successfully ")
        else:
            print("Error try again :")
   
    option()
    
    
def deleteinventory():
    id=int(input("Enter the id to delete the data :"))
    st="delete from vehicledata where id in ( (%s),(%s))"
    data=cur.execute(st,(id,id))
    st1="select * from vehicledata where id=%s"
    cur.execute(st1,id)
    con.commit()
    if(data==True):
           print('This vehicle has been removed')
           print(cur.fetchone())
    else:
        print("Error try again :")
  
    option()
    
def exportinventory():
    con = pymysql.connect("localhost","root","sm18","inventory")
    cur=con.cursor()
    cur.execute("select * from vehicledata")
    data=cur.fetchall()
    with open('C:\\Users\\Sanjana\\Desktop\\vehicle.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        # Add the header/column names
        header = ['id','category','make', 'color', 'mileage','year']
        writer.writerow(header)
        # Iterate over `data`  and  write to the csv file
        for row in data:
            writer.writerow(row)
    print ("The data has been successfully exported")
  
    option()

def bargraph():
    data=pd.read_csv("C:\\Users\\Sanjana\\Desktop\\vehicle.csv")
    data.head()
    print(data)
    df=pd.DataFrame(data,columns=['id','category','make','color','mileage','year'])
    plt.xlabel('Make of Car')
    plt.ylabel('Mileage of Car')
    plt.title('Bar Chart to Show Mileage of Cars')
    x=data.make
    y=data.mileage
    plt.bar(x,y)
    plt.show()

    option()

main()


