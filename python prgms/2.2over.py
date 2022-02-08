list1=[]
n=int(input("enter the limit:"))
for i in range(n):
    a=int(input("enter the value:"))
    list1.append('over'if a>100 else a)
    print(list1)
