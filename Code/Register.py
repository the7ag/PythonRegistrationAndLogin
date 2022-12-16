from datetime import date                                                       #to calculate the age
import json                                                                     #to work with txt files and dictionaries
import re                                                                       #for the format of the email and username
from cryptography.fernet import Fernet                                          #for password encryption
fofo=open("key.key","rb")         
key=fofo.read()                                                                 #the key used to encrypt any password
fofo.close()                                                                    #close the file
def register():
    """
    This is the register Function
    it's called only by the main start function
    it takes the user input and save it into dict
    and after that it saves it in a txt file using json module
    """
    myDic={                                                                     #User Dictionary
        "Firstname":"",
        "Lastname":"",
        "Username" : "",
        "Password" : "",
        "Email" : "",
        "Phone" : "",
        "Birthday":"",
        "Age": ""
    }
    with open('database.txt') as db:
        data = db.readlines()                                                   #save the every line in the file in data
    
    """
    First name input
    """
    flag=True                                  
    while(flag):
        try:
            regex = r'\b[A-Za-z]{2,}\b'                                          #Firstname format                            
            myDic["Firstname"]=input("Please Enter Your First Name : ")                                                            
            if(not re.fullmatch(regex, myDic["Firstname"])):                      #check if the input matches the format                  
                print("Invalid Username please enter [A-Z a-z] only")
                continue 
            flag=False 
        except ValueError as err:
            print(err)
    
    """
    Last name input
    """
    flag=True
    while(flag):
        try:
            regex = r'\b[A-Za-z]{2,}\b'                                              #Lastname Format               
            myDic["Lastname"]=input("Please Enter Your Last Name : ")                                                            
            if(not re.fullmatch(regex, myDic["Lastname"])):                   
                print("Invalid Username please enter [A-Z a-z] only")
                continue 
            flag=False 
        except ValueError as err:
            print(err)
    
    """
    Username input
    """
    flag=True                                   
    while(flag):
        try:
            regex = r'\b[A-Za-z0-9._%+-]{2,}\b'                                    #the format for username
            notfound=False                                                         #this flag is sit high if the username already exists
            myDic["Username"]=input("Please Enter Your User Name : ")               #read the username
            for line in data:                                                       #for every line in the database file
                js=json.loads(line.strip())                                         #read every line as it's own dict
                if(js["Username"]==myDic["Username"]):                              #if you found the user name in the files
                    print("Username Already Exist")                      
                    notfound=True                                                   #set the flag high
            if notfound:
                continue                                                            #repeat the input untill a unique user is entered
            if(not re.fullmatch(regex, myDic["Username"])):                          #match to non random user format
                print("Invalid Username, please enter [A-Z a-z 0-9 . _ % + -] only")
                continue                                                            #repeat untill good format is entered
            flag=False                                                              #if no repeats happens stop the loop
        except ValueError as err:
            print(err)
    
    """
    Password input
    """
    flag=True                                                                       #same as above
    while(flag):
        try:
            myDic["Password"]=input("Please Enter Your Password : ")  
            password=input("Please Confirm Your Password : ")
            if(password!=myDic["Password"]):
                print("Wrong Password")                                             #same password twice
                continue
            if(len(myDic["Password"])<8):
                print("Please Enter At Least 8 Charcters")
                continue
            flag=False;
            Encoded=myDic["Password"].encode()                                     #turn the password int \b
            f=Fernet(key)                                                           #make an object of fernet
            encrypted=f.encrypt(Encoded)                                            #encrypt the password using fernet
            myDic["Password"]=encrypted.decode()                                    #turn the encodded bits to String again to save it
        except ValueError as err:
            print(err)
    
    """
    Email input
    """
    flag=True
    while(flag):
        try:
            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'          #the format for the email
            notfound=False                                                          #same as the username
            myDic["Email"]=input("Please Enter Your Email : ")
            for line in data:
                js=json.loads(line.strip())
                if(js["Email"]==myDic["Email"]):
                    print("Email Already Exist")
                    notfound=True
            if notfound:
                continue
            if(not re.fullmatch(regex, myDic["Email"])):
                print("Invalid Email")
                continue
            flag=False
        except ValueError as err:
            print(err)
    
    """
    Phone number input
    """
    flag=True
    while(flag):
        try:
            notfound=False
            myDic["Phone"]=input("Please Enter Your Phone Number : ")
            for line in data:
                js=json.loads(line.strip())
                if(js["Phone"]==myDic["Phone"]):
                    print("Phone number Already Exist")
                    notfound=True
            if notfound:
                continue
            if myDic["Phone"][:2]!='01' or len(myDic["Phone"])<11:                                              #to make sure that the phone number is in the right eg format
                print("Invalid Number")
                continue
            flag=False
        except ValueError as err:
            print(err)
    
    """
    Year of birth input
    """
    flag=True
    while(flag):
        try:
            year=int(input("Pleas Enter The Year You Were Born : "))
            if year>2022 or year<1900: #To input the right Year
                print("Invalid Year")
                continue
            flag=False
        except ValueError as err:
            print(err)
    
    """
    month of birth input
    """

    flag=True
    while(flag):
        try:
            month=int(input("Pleas Enter The Month You Were Born : "))
            if month>12 or month<0: #to input the right month
                print("Invalid Month")
                continue
            flag=False;
        except ValueError as err:
            print(err)
    """
    day of birth input
    """
    flag=True
    while(flag):
        try:
            day=int(input("Pleas Enter The Day You Were Born : "))
            if day>30 or day<0: #to input the right day
                print("Invalid day")
                continue
            flag=False;
        except ValueError as err:
            print(err)
    birthday=date(year,month,day)                                       #make a date object of year month and day
    myDic["Birthday"]=str(year)+"-"+str(month)+"-"+str(day)             #save the birthday as string
    today=date.today() #get today's date
    age=(today.year-birthday.year)-((today.month,today.day)<(birthday.month,birthday.day))  #to get the right age we sub the years and check if the day is passed or not
    myDic["Age"]=age                                                    #save the age
    """
    Saving the dict in the database if all the above is correct
    """
    with open('database.txt', 'a') as database:                         #open the file as database
        database.write(json.dumps(myDic))                               #write the dict in the file using json
        database.write("\n")                                            #write a new line
        print("Account Created Successfully !!!!!")
    return