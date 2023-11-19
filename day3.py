print("Day3")
response="yes"
while response=="yes"or response=="y"or response =="yeah" or response =="Y":
    name=input("Enter your name:")
    num=float(input ("Enter your Percentage (without % symbol):"))
    if num>=90 and num <=100:
        print("A grade")
    elif num>=80 and num<=90:
        print ("B grade")
    elif num>=70 and num<=80:
        print ("C grade")
    elif num >=60 and num<= 70:
        print ("D grade")
    elif num >= 50 and num <=60:
        print ("@2nd dvision..")
    elif num >=0 and num<=50:
        print("Oops,Sorry ,Fail....")
    else :
        print("invalid number,Scam caught...Lol!!")

    response = str(input("\n \n do you want to continue (Yes\No):"))
    print ("\n**program ends.. Thanku**")


      

'''
print ("Day 3 ")
print("reverse numbering")
i=5
while i>0 :
    print(i)
    i=i-1
print("problem ends! ")
print("\n\nforword numbring")
i=1
while i<6:
    print(i)
    i = i+1
print("problem ends !")
print("\n\n Nested loops")
for i in range (6):
    for j in range(1,i+1):
        print ("*",end = ",")
    print("")
print("problem solved")
for i in range (6):
    for j in range(1,i):
        print ("*",end = ",")
    print()
print("..")
'''

