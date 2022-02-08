startYear = int(input("enter the starting year"))
endYear = int(input("enter the last year"))
for year in range(startYear, endYear):
    if (0 == year % 4) and  (0 != year % 100) or(0 == year % 400):
        print(year)