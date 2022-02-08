n=input("Enter the string:")
a={}
c=0
for i in n:
    for j in n:
        if i == j:
            c=c+1
    a.update({i:c})
    c=0
print(a.items())