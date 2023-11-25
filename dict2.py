def updating(s):
    p=input("Enter your updateing key name")  # p storing key name
    s[p]=int(input("Add phone no."))      #changing data of key(p)
def display(s):
    k = s     # k is only temperary
    if k == 0:
        print("\t\tEmpty contact list")
    else:
        for i in k.keys():
            print("\t",i,"=>",k[i])   #show dict in a manner way
def delet(s):
    k=input("Enter your deleting key name") #asking user to deleting key
    print("\tyour",k,"data has been deleted")
    s.pop(k)     #deleting key(k) from the dict
def choic():
    print("\t1 for Display contects\n\t2 for update contacts\n\t3 for add contects")
    print("\t4 for deleting contects\n\t5 for exit contect manager")
def add(a):
     dict1 = a   #a is empty or previous dict
     dict2={}    # temprary dict
     loop=int(input("Enter your size of dict"))
     for i in range(0,loop,1):
          name=input("Enter your name:-")
          pn=int(input("Enter your phone number:-"))
          if len(dict1) == 0:
               dict1[name]=pn
          else:
               dict2[name]=pn    #temperay dict that store key or data
          dict1.update(dict2)     #adding dict1 and dict 2 in dict1
     print("\tYour contact has been added---|")
     return dict1     #dict1 storing in s
    
response ="yes"
a = {}    #the empty dict where the contect are storing
while response in["yes","YES","y","Yes"]:
    print("===="*15)  #to show output in proper way
    print("Enter your choice according your need")
    choic()
    choice=int(input("Enter your choice-:"))
    print("==="*15)
    if(choice == 1):
        display(s)
    elif(choice == 2):
        updating(s)  # updating key or adding new key in dict
    elif(choice == 3):
        s=add(a)     # s is a dict that is first created or added new contect
    elif (choice == 4):
        delet(s)     # poping key from the dict
    elif(choice != 5):     #when user put wrong choice
        print("Wrong choice check again")
    else:
        break
    response=input("Do you want to continu the program(Y/N)")
print("---Program ends hear!!---")#after No or 5
    
    
