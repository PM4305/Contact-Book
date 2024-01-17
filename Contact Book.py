import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='root',database='contact')
cur=con.cursor()
#cur.execute("create database contact")
#cur.execute("create table details(Name varchar(100),Phone_No char(10),Email varchar(50),Address varchar(100))")
#con.commit()
def MainMenu():
    print("\n1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    n=int(input("\nEnter Your Choice: "))
    if n==1:
        AddContact()
    elif n==2:
        ViewContactList()
    elif n==3:
        tup=SearchContact()
        print("Name     Phone Number     Email       Address\n")
        for row in tup:
            print(row[0],"      ",row[1],"  ",row[2],"  ",row[3])
        print("\n1. MainMenu\n2. Exit")
        m=int(input("Enter your Choice: "))
        if m==1:
            MainMenu()
        else:
            exit()
    elif n==4:
        UpdateContact()
    elif n==5:
        DeleteContact()
    else:
        print("\n!!Wrong Input!!\n")
        MainMenu()
        
def AddContact():
    ch='y'
    while ch=='y':
        print("\nEnter Contact Details: \n")
        name=input("Enter Name: ")
        mob=input("Enter Phone Number: ")
        email=input("Enter Email: ")
        addr=input("Enter Address: ")
        cur.execute("insert into details values('{0}','{1}','{2}','{3}')".format(name,mob,email,addr))
        con.commit()
        ch=input("\nDo you want to add more contacts(y/n): ")
    print("\n1. MainMenu\n2. Exit")
    m=int(input("Enter your Choice: "))
    if m==1:
        MainMenu()
    else:
        exit()

def ViewContactList():
    print("\n                Contact List\n")
    cur.execute("select * from details")
    contacts=cur.fetchall()
    print("Name     Phone Number     Email       Address\n")
    for row in contacts:
        print(row[0],"      ",row[1],"  ",row[2],"  ",row[3])
    print("\n1. MainMenu\n2. Exit")
    m=int(input("Enter your Choice: "))
    if m==1:
        MainMenu()
    else:
        exit()

def SearchContact():
    print("\nSearch Contact By: \n")
    print("1. Name\n2. Phone Number\n3. Email")
    n=int(input("\nEnter Your Choice: "))
    if n==1:
        name=input("Enter Name of Contact: ")
        cur.execute("select * from details where Name='{0}'".format(name))
    elif n==2:
        mob=input("Enter Phone Number of Contact: ")
        cur.execute("select * from details where Phone_No='{0}'".format(mob))  
    elif n==3:
        email=input("Enter Email of Contact: ")
        cur.execute("select * from details where Email='{0}'".format(email))  
    else:
        print("\n!!Wrong Input!!\n")
        MainMenu()
    contact=cur.fetchmany()
    if len(contact)!=0:
        return contact
    else:
        print("\n!No Such Contact Found!\n")
        MainMenu()
        
def UpdateContact():
    ch='y'
    while ch=='y':
        tup=SearchContact()
        print(tup)
        print("\nEnter the Detail to be Updated: \n")
        print("1. Name\n2. Phone Number\n3. Email\n4. Address")
        n=int(input("\nEnter Your Choice: "))
        if n==1:
            name=input("Enter Updated Name of Contact: ")
            cur.execute("update details set Name='{0}' where Phone_No='{1}'".format(name,tup[0][1]))
            con.commit()
        elif n==2:
            mob=input("Enter Updated Phone Number of Contact: ")
            cur.execute("update details set Phone_No='{0}' where Name`='{1}'".format(mob,tup[0][0]))
            con.commit()
        elif n==3:
            email=input("Enter Updated Email of Contact: ")
            cur.execute("update details set Email='{0}' where Phone_No='{1}'".format(email,tup[0][1]))
            con.commit()
        elif n==4:
            addr=input("Enter Updated Address of Contact: ")
            cur.execute("update details set Address='{}' where Phone_No='{}'".format(addr,tup[0][1]))
            con.commit()
        else:
            print("\n!!Wrong Input!!\n")
            MainMenu()
        ch=input("\nDo you want to update more contacts(y/n): ")
    print("\n1. MainMenu\n2. Exit")
    m=int(input("Enter your Choice: "))
    if m==1:
        MainMenu()
    else:
        exit()
    
def DeleteContact():
    ch='y'
    while ch=='y':
        tup=SearchContact()
        print("\nName     Phone Number     Email       Address\n")
        for row in tup:
            print(row[0],"      ",row[1],"  ",row[2],"  ",row[3])
        j=input("\nAre you sure you want to delete the contact (y/n): ")
        if j=='y':
            cur.execute("delete from details where Phone_No={}".format(tup[0][1]))
            con.commit()
        else:
            print("\n!Deletion Aborted!\n")
            MainMenu()
        ch=input("\nDo you want to delete more contacts(y/n): ")
    print("\n1. MainMenu\n2. Exit")
    m=int(input("Enter your Choice: "))
    if m==1:
        MainMenu()
    else:
        exit()

print("                   Contacts Book\n")
MainMenu()

    
    
        
