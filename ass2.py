lis=[]
for i in range(1,6,1):
      a=int(input("Enter your integer number:"))
      lis.append(a)
x=0
y=0
for i in range(len(lis)):
     for j in range(x+1,len(lis),1):
            if lis[j] == lis[x]:
                print("Repeted element is ",lis[x])
                y += 1
                break;
            else:
                pass
            
     x +=1
if y == 0:
    print("Not duplicte")
