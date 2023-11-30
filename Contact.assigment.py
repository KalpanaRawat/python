print("making a contact list...")
print("="*50)
def A():
    print("="*50)
    print("1.---Display Contact---")
    print("2.---Update Contact---")
    print("3.---Add Contact---")
    print("4.---Delete Contact---")
    print("5.---Exit the Contact manager---")
    print("="*50)
l=[ "Aarti=9090,Babita=8989,Chandu=6767"]
response = "yes"
while response in ["Y","y","yes","yes","yeah"]:
    A()
    choise =int(input ("Enter your choise According to the about information...:______"))
    if choise==1:
        print("\n\t---Display contact---")
        print(l)
            
          
    elif choise == 2:
        print("\n\t---Update Contact---")
        name=input("Enter your name:")
        BB=int(input("Enter your number.."))
        dd=print({name},"=",{BB})
        BB=print (l.append(dd))
        print("*"*5,"Contact has been updated..!","*"*5)

        
    elif choise ==3:
        print("\n\t---Add Contact---")
        BB=input("Enter your name:=")
        CC=int(input("Enter your phone number:="))
        B={"Name":BB,"Phone number":CC}
        print(B)
        #print(AA.append(B))
        print("-"*5,"Contact has been updated","_"*5)
        #print("Hello Mr.",BB,"your Number is=",CC)
        
        
    elif choise ==4:
        DD=input("Enter your name")
        #print(del(DD))
        print("\n\t---Delete contact---")

        
    elif choise==5:
        print("\n\t---Exit the Contact manager---")
        break

    
    else:
        print("\n\t---OOps...Sorry...try again...---")
    print()
    response = input("Do you want to continue?...")
print("\n****Contact manager closed****")
                    


