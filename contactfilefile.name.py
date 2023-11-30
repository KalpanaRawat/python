def updat(r):    #Updating the contact by name or adding single new contact
    k={}          #Using to store input given by user as a dict
    name=input("Enter your name")
    pn=int(input("Enter pn"))
    k[name]=pn
    r.update(k)    #updating user given input in dict
    with open("contact.txt",'r') as file:
        file.read()               #only for check
        file.close()
    with open("contact.txt",'w') as file:
        s=file.write(str(r))        #updating data in contact file
    file.close()
    print("Your contact has been update")
    print("___"*15)
    return r      # giving new dict
def contact_add(store_value):
    element=int(input("enter your adding element total no.:"))#only for loop
    dict1=store_value    #storing contact file data
    dict2={}             #temprary data
    for i in range(element):
        name=input("Enter your name")  #accepting data 
        if name in dict1.keys():
           print("already exist in contact")  #only for conform
        else:
            pn=int(input("Enter phone no."))
            dict2[name]=pn                #storing temprary data
        dict1.update(dict2)            #storing all data in one dict
    return dict1

def contact_display(store):
    if store == {}:           #for clear understanding
        print("No data hear")
    for i in store.keys():
          print("\t\t",i,"=>",store[i]) #giving output in proper way
    with open("contact.txt",'w') as f:
        f.write(str(store))             #updating contact file
        f.close

  #create contact file with atleast {} input to run this program

contact1=0       #only veriable 
with open("contact.txt",'r') as file:
    contact1=file.read()               # 1st step to accept data from contact file
    contact=eval(contact1)
    file.close()      #converting contact file data in dict form
for i in contact.keys():
            #giving contact file ouput
    print("\t\t",i,"=>",contact[i])
    file.close()
def choice():                   #to user confert
    print("__"*30)
    print("\t1 for add contact in contact file")
    print("\t2 for display contact ")
    print("\t3 for update contact")
    print("\t4 for exit")
    print("--"*30)
store=contact    #A contact file data
response="yes"   #To start loop
store1=contact    #Extra veraible to store contact file data
while response in ["yes","y","YES","Yes","Y"]:
    choice()
    step=(input("Enter your choice according your need:"))  # a choice 
    print("__"*30)
    if step == '1':
        store1=contact_add(store) #calling function with file data
    elif step == '2':
        if store1 != {} :  #calling display function 
            contact_display(store1) 
        else:
            contact_display(store) #calling function 
    elif step == '3':
         store2=updat(store1)    #calling update function with stored data by add function
    elif step != '4':
        print("Wrong choice")  #Only for clear program
    else:
        break         #To go out from the loop
    print("__"*30)
    response = input("Do you want to continue the program (y/n):")
print("__"*30)
print("Program ends hear!!")
input()
