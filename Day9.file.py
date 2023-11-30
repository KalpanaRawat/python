name= input("Enter your name: ")
msg = input("Enter your massage..: ")
with open("userdata.txt",'a') as file:
    file.write(name+"=>"+msg+"\n")
    file.close()
try:
    with open("userdata.txt",'r')as file:
        data=file.read()
        print(data)
        file.close()
except:
    print("Cannot open the file!")
    
