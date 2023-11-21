
def rectangle(length,breadth):#choice 1 (a=1) Rectangle Area and perimater
     print("Area of Rectangle is ", length*breadth,"cm**2")
     print("Perimater of Rectangle is ",2*(length + breadth),"cm")

def circule(radius):  #choice 2 (a=2) Circule area and circumference
    PI=3.14
    print(radius," redius circule  area is",(PI*(radius**2)))
    print(radius," redius circule circumference is",2*PI*radius)

def check(char):      #choice 3 (a=3) calculating character in given line
    # c ,d used for calculate character and digit
    c = 0
    d = 0
    for i in char:
        if i.isalpha():
            c += 1
        elif i.isdigit():
             d += 1
        else:
             pass
    print("Total character in your given line -: ", c)
    print("Total digit in your line is -:",d)
    print("Total length of your line is ",len(char))
    again=input("Do you want to continu the program of a chek character in a line (yes/no)-:")
    if again == "yes" or again == "y" or again == "yeaa":
         char=input("Enter your line")
         check(char)
    else:
         pass
        
def triangle(x,y,z):  # choice 4 (a=4) checking traingle type
    if x == y or y == z or x == z :
        if(x == z and y == z):
            print(" given sides are show it is equilateral triangle")
        else :
            print(" given sides are show it is isosceles triangle")
    else :
        print(" given sides are show it is equilateral scalene triangle")

def temperature(celsius):  # choice 5 (a=5) converting temperature celsius to fahrenhiet
    print("your temperature",celsius,"celsius in fahrenhiet is",(celsius*9//5)+32) 


print("Enter your choice according no.\n")
print("1 for Rectangle")
print("2 for Circule")
print("3 for check charcater in line")
print("4 for check triangle")
print("5 for temperature\n")
a=int(input("Enter your choice:"))#a is a choice for condition
print()
if(a==1):
    length=float(input("Enter your lenght of rectangle in centimeter:"))
    breadth=float(input("Enter your breadth of rectangle in centimeter:"))
    rectangle(length,breadth)
elif(a==2):
    radius=float(input("Enter your circule redius"))
    circule(radius)
elif(a==3):
    char=input("Enter your line:")
    check(char)
elif(a==4):  #x,y,z  used for triangle side
    x=float(input("Enter your first side of triange:"))
    y=float(input("Enter your second side of triange:"))
    z=float(input("Enter your Third side of triange:"))
    triangle(x,y,z)
elif(a==5):
    celsius=float(input("Enter your temperature in celsius"))
    temperature(celsius)
    
