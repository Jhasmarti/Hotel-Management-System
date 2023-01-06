#!/usr/bin/env python
# coding: utf-8

# # Hotel Managemnet system

# In[ ]:


import os
import platform 
import mysql.connector as con
import pandas as pd
import datetime


# In[2]:


global z
global s
mydb=con.connect(user='root',password='1234567890',host='localhost',database='hotel')
mycursor=mydb.cursor()


# In[3]:


def registercust():
    l=[]
    custname=input("enter name:")
    l.append(custname)
    addr=input("enter address:")
    l.append(addr)
    indate=input("enter check in date(dd/mm/yyyy):")
    l.append(indate)
    outdate=input("enter check out date(dd/mm/yyyy)")
    l.append(outdate)
    cust=(l)
    sql="insert into custdata(custname,addr,indate,outdate)values(%s,%s,%s,%s)"
    mycursor.execute(sql,cust)
    mydb.commit()


# In[4]:


def roomtypeview():
    print("Do you want to see room type Enter 1 for yes:")
    ch=int(input("Enter your room type choice:"))
    if ch==1:
        sql="select * from roomtype"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
            


# In[5]:


def roomrent():
    print("We have the following rooms for you:-")
    print("1. typeA --> rs 1000 PN\-")
    print("2. typeB --> rs 2000 PN\-")
    print("3. typeC --> rs 3000 PN\-")
    print("4. typeD --> rs 4000 PN\-")
    x=int(input("Enter your choice please -->"))
    n=int(input("For How Many Nights Did You Stay."))
    if(x==1):
        print("you have opted room type A")
        s=1000*n
    elif(x==2):
        print("you have opted room type B")
        s=2000*n
    elif(x==3):
        print("you have opted room type C")
        s=3000*n
    elif(x==4):
        print("you have opted room type B")
        s=4000*n
    else:
        print("please choose a room")
    print("your room rent is=",s,"\n")
    


# In[6]:


def restaurentmenuview():
    print("Do you want to see menu available :Enter 1 for yes:")
    ch=int(input("Enter your choice"))
    if(ch==1):
        sql="select *  from restaurent"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)


# In[7]:


def orderitem():
    global s
    print("Do you want choose menu available: Enter 1 or yes:")
    ch=int(input("Enter your choice"))
    if(ch==1):
        sql="select *  from restaurent"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x)
    print("DO you want to purchase from above list :enter your choice:")
    d=int(input("Enter your choice:"))
    if(d==1):
        print("You have ordered tea")
        a=int(input("Enter quantity"))
        s=10*a
        print("you amount for tea is:",s,"\n")
    elif(d==2):
        print("You have ordered coffee")
        a=int(input("Enter quantity"))
        s=10*a
        print("you amount for coffee is:",s,"\n")
    elif(d==3):
        print("You have ordered colddrink")
        a=int(input("Enter quantity"))
        s=20*a
        print("you amount for colddrink is:",s,"\n")
    elif(d==4):
        print("You have ordered samosa")
        a=int(input("Enter quantity"))
        s=10*a
        print("you amount for samosa is:",s,"\n")
    elif(d==5):
        print("You have ordered Sandwich")
        a=int(input("Enter quantity"))
        s=50*a
        print("you amount for sandwich is:",s,"\n")
    elif(d==6):
        print("You have ordered dhokla")
        a=int(input("Enter quantity"))
        s=30*a
        print("you amount for dhokla is:",s,"\n")
    elif(d==7):
        print("You have ordered Kachori")
        a=int(input("Enter quantity"))
        s=10*a
        print("you amount for kachori is:",s,"\n")
    elif(d==8):
        print("You have ordered milk")
        a=int(input("Enter quantity"))
        s=20*a
        print("you amount for milk is:",s,"\n")
    elif(d==9):
        print("You have ordered noodles")
        a=int(input("Enter quantity"))
        s=50*a
        print("you amount for noodles is:",s,"\n")
    elif(d==10):
        print("You have ordered pasta")
        a=int(input("Enter quantity"))
        s=50*a
        print("you amount for pasta is:",s,"\n")
    elif(d==11):
        print("You have ordered pizza")
        a=int(input("Enter quantity"))
        s=80*a
        print("you amount for pizza is:",s,"\n")
    elif(d==12):
        print("You have ordered burger")
        a=int(input("Enter quantity"))
        s=50*a
        print("you amount for burger is:",s,"\n")
    else:
        print("please enter your choice from the menu")


# In[8]:


def laundarybill():
    global z
    print("DO you want to see rate for laundary : enter 1 for yes:")
    ch=int(input("Enter your choice"))
    if(ch==1):
        sql="select *  from laundary"
        mycursor.execute(sql)
        rows=mycursor.fetchall()
        for x in rows:
            print(x) 
    y=int(input("Enter your number of clothes->"))
    z=y*10
    print("Your laundary bill: ",z,"\n")
    return z


# In[9]:


def lb():
    y=int(input("Enter your number of clothes->"))
    z=y*10
    print("Your laundary bill: ",z)


# In[10]:


def viewbill():
    registercust()
    roomrent()
    orderitem()
    lb()


# In[ ]:


def Menuset():
    print("Enter 1: to Enter customer data")
    print("Enter 2: to view roomtype")
    print("Enter 3: to calculating room bill")
    print("Enter 4: to viewing restaurent menu")
    print("Enter 5: to restaurent bill")
    print("Enter 6: to laundary bill")
    print("Enter 7: to complete bill")
    print("Enter 8: to Exit")
    try:
        pass
    except valueError:
        exit("\n hi that not a number")
    
    userinput=int(input("enter your choice"))
    if(userinput==1):
        registercust()
    elif(userinput==2):
        roomtypeview()
    elif(userinput==3):
        roomrent()
    elif(userinput==4):
        restaurentmenuview()
    elif(userinput==5):
        orderitem()
    elif(userinput==6):
        laundarybill()
    elif(userinput==7):
        viewbill()
    elif(userinput==8):
        quit()
    else:
        print("Enter correct choice")
Menuset()
    


# In[ ]:


def runagain():
    runagn=input=("\n Do you want run again y/n:")
    while(runagn.lower()=='y'):
        if(platform.system()=="windows"):
            print(os.system('cls'))
        else:
            print(os.system('clear'))
        Menuset()
        runagn=input("\n want to run agin y/n:")


# In[ ]:


runagain()


# In[ ]:




