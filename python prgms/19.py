p=int(input("Enter the principal amount:"))
r=int(input("Enter the rate of interest:"))
t=int(input("Enter the time in the years:"))
A=p*(pow((1+r/100),t))
print("amount=",A)
ci=A-p
print("compount interest=",ci)
