'''
def read_file(Login):
    try:
        with open (login , 'r') as login:
            data = login.read()
            return login
        except user not found Error:
            return "Sorry.. User not found."
    try:
        with open (login , 'a') as login:
            data = login.read()
            return login
        except user not found Error:
            return "Sorry.. User not found."
'''
print("Registration Login information page..!!")
name= input("Enter your name: ")
Course = input("Enter your Course..: ")
ff= input ("Enter your fathers name..:")
mm= input("Enter your Mothers name..:")
En=input("Enter your Enrollment number..:")
num=input("Enter Total numbers..")
DOB=input("Enter your Date of Birth..!")
i=int("Enter your Enrollment number..!:=")

with open("login",'a') as login:
    login.write(name+"=>"+Course+"\n")
    login.write("Fathers name"+"=>"+ff+"\n")
    login.write("Mothers name"+"=>"+mm+"\n")
    login.write("Enrollment number"+"=>"+En+"\n")
    login.write(name+"=>"+Num+"\n")
    login.write("Date of birth"+DOB+'\n')

          
try:
    with open("login",'r')as login:
        data=login.read()
        print(data)
        login.close()
except:
    print("Cannot open the file!")
    
