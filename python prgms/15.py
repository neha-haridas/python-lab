string=str(input("Enter the string:"))
a=string[0]
for c in string[1:-1]:
    if c==a:
        b=string.replace(c,"$")
print(a+b[1:])