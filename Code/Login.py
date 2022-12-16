import re                                                                          #to make sure the format is write
import json                                                                        #to import txt as dict
from cryptography.fernet import Fernet                                             #to decrypt the password
file=open("key.key","rb")                                                          #using the same key
key2=file.read()
file.close




def login():   
    """
    This is the main login function
    it's called only by the main start function
    it canno't be called if there's no users in the database
    """                                                                    #The login function
    with open('database.txt') as db:                                               #check if there is any users in the database
        size = len(db.readlines())
        if size<=0:
            print("No Users Accounts is made yet") 
            return

            """the user dict"""
    userDic={ #create a dict for the new input
    "User":"",
    "Password":""
    }
    userFlag=False
    userPass=False
    with open('database.txt') as db:
        data = db.readlines()                                                      #save the lines in data
    """
    The username or email input
    """
    flag=True
    while(flag):
        try:
            userDic["User"]=input("Please Enter Your Username/Email : ")            #Login username
            for line in data: #for everyline
                js=json.loads(line.strip())
                if(js["Username"]==userDic["User"])or(js["Email"]==userDic["User"]): #if input matched the username or email
                    userFlag=True                                                    #found the user
                    
                    """
                    If you found that username enter his password and it won't comeout from this code
                    """
                    
                    while(flag):                                                     #search for the password at this partiuclar user
                        try:
                            userDic["Password"]=input("Please Enter Your Password : ") #ask for the password
                            #########################   Decripton   ###################
                            f2=Fernet(key2)                                             #create and object from the fernet
                            Decrypted=f2.decrypt(js["Password"].encode())               #we need to encode the js from string back to \b then we decrypt it
                            original=Decrypted.decode()                                 #then we decode it from \b to str again
                            if(original==userDic["Password"]):                          #we compare them and if it's equal we set the Flag
                                userPass=True
                            if not userPass:
                                print("Wrong Password Please Enter Correct Password !!!!")
                                continue
                            flag=False
                        except ValueError as err:
                            print(err)
            """User Not Found !!!!"""
            if not userFlag:                                                            #if user not found
                print("User Not Found Enter A Right Username")
                continue
            flag=False
        except ValueError as err:
            print(err)
    """Successfully found both of them """
    if(userPass and userFlag):                                                      #if the user and pass are correct
        print("Logged in Successfully")
        flag=True
        while(flag):
            try:
                state=input("What You Want to do ? 1 - return \n")                  #logged in success
                if(state=='1'):
                    return
                else:
                    continue
                flag=False
            except ValueError as err:
                print(err)