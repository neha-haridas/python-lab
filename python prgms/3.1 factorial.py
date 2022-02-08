
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("for negative number factorial doesn't exist")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)
num=int(input("enter a number:"))
