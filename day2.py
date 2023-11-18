print("Day 2 Python class")



print ("Conditional")
print("Question=had you done your homework?")
ans = str(input("tell Your ans..."))
if ans =="yes" or ans=="yeah":
    print("You will get a chocklet.")
elif ans in ["yes", "yeah", "yo", "y"]:
    print("you will get something nice")
elif ans =="No" or "no" :
    print ("You will not get the chocklet..")
else :
    print ("You should Done your homework first!!..")


    
print("\n\nFor loop")
print ("\nPrinting numbers in assinding order")
for i in range (0,11,1):
    print(i,end = ",",)
print("\nprinting numbers in decending order")
for j in range (11,0,-1):
    print(j,end=",")

    '''
print ("\n numbers in the from of *")
for k in range(1,6,1):
    print("*",end = ",")
'''

print ("\n multiples of 11 in assiding order:")
for l in range (0,122,11):
    print(l,end = ",")
print ("\n multiples of 11 in decending order:")
for l in range (122,0,-11):
    print (l,end = ",")


print("Home Work of Day 2 class..")
print ("\nlist of numbers from 1 to 10")
for m in range(1,11,1):
    print (m,end=",")
print("\n list of reverse numbers from 10 to 1")
for n in range(10,0,-1):
    print (n,end=",")
    
