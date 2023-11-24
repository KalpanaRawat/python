def grade(per):
    x = per
    if x >= 80 and x <= 100 :
        print("you got A grade\n")
    elif x >= 60 and x < 80 :
        print("You got B grade")
    elif x >= 40 and x < 60 :
         print("You got C grade")
    elif x >=0 and x <40 :
         print("Sorry you failed")
    else :
      print("You got wrong persantaze")
def per(total,no):
   # print(total,no)
    per=total/no
    print("your persentaze is:",per)
    return per
def number(subject):
    lst=[]
    add=0
    for i in subject:
        print("Enter",i,end=" ")
        a=int(input("Number"))
        if a >=0 and a <= 100:
            lst.append(a)
        else:
            print("Wrong no. entered!!")
    for i in lst:
        add=add+i   
    return add 
response="YES"
while response in ["YES","yes","y","Yes"]:
    print("=="*20)
    name=input("Enter your name:")
    clas=int(input("Enter your class:"))
    if clas < 1 and clas >12:
        print("wrong class")
    subjects=input("Enter your subject(seprate by comma)")
    subject=subjects.split(",")
    length=len(subject)
    x=number(subject)
    print("=="*20)
    print("hello ",name,"\n","Your class is",clas,"Your subjects are",subject)
    print("Total marks is",x)
    y=per(x,length)
    grade(y)
    print("--"*20)
    response=input("Do you want to continue(Yes/No)")
