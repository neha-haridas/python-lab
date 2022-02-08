n=int(input("Enter the number"))
c=[]
for i in range(1,n+1):
    for j in range(1,i+1):
        if i*j==n:
            c.append(i)
            c.append(j)
print("factors of "+str(n)+" :")
for i in c:
    print(i)