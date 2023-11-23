a=int(input("Enter your number of row:"))

a=a+1
x=1
          #printing natural no. in pyramid <17
print()
print("--"*15)

for i in range(0,a):
     if(x<17):
         for j in range(0,2*i+1):
             print(x,end=" ")
             x+=1   
         print()
print()

            #printing pattern semi pyramid
print("--"*15)
for i in range(1,a+1):
    for j in range(1,i):
        print(j,end=" ")
    print()
print()    

            # printing pattern (Horizantal table)
print("--"*15)
for i in range(0,a):
    for j in range(0,i+1):
        print(i*j,end=" ")
    print()    
print()

            # printing inverted pyramids
print("--"*15)
for i in range(1,a+1):
    for j in range(a-i,0,-1):
        print(i,end=" ")
    print()

print("--"*15)
