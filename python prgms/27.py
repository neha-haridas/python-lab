n=int(input("Enter the no of elements:"))
a=[]
for x in range(0,n):
    a.append(input("Enter the word: "))
c=0
for i in a:
    if len(i)>c:
        c=len(i)
        longest=i
print("longest word is:",longest,"and length of longest word is:",len( longest))
