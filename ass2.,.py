num=int(input("Enter your no."))
for i in range(1,11,1):
    print(num,"*",i,"=",num*i)
print()
print("Factor of a number are-:",end=" ")
for i in range(1,num+1,1):
    if(num % i == 0):
       print(i,end=" ")
