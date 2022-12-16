"""
This app is made by Mohamed Ali Bayoumi
"""


import Register
import Login
'Import the two files'


#The Function That's called when quit is choosen
def quitApp():
    """
    This is the function that is called when you want to quit the app
    it needs only one answer y\n
    """
    flag=True                                     #to keep asking for the input untill right input is reached
    while(flag):
        try:
            m=input("Are You sure? y\\n : ")
            if(m=='n'):
                flag=False                        #if no close the function if yes stop the program
                return
            elif(m=='y'):
                exit()
            else:
                print("Enter y\\n only!!")         # if you put anyother letter
                continue
        except ValueError as err:
                print(err)

def start(): 
    """
    This is the home screen of the app
    it'll always come back to this folder nomatter what happens
    it needs only one int input
    """                                       #the home page of the prorgam
    flag=True
    while(flag):
        try:
            x=int(input("Choose what you want to do : 1- Register 2- Login 3- Quit \n"))  #first input
            if x==1:
                flag=False
                Register.register()                 ##call the register function
            elif x==2:
                flag=False
                Login.login()                        #call the login function
            elif x==3:
                flag=False
                quitApp()                           #end app
        except ValueError as err:
            print(err)
            continue
while True:                                         ##keep the program running after the any function is done
    start()          
