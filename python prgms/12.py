n=int(input("enter the number of integers"))
a=[]
for i in range(0,n):
     x=int(input("enter the integers"))
     if(x>100):
         a.append("over")
     else:
        a.append(x)
print(a)
