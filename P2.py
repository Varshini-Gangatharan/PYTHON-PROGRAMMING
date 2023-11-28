year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year,"is a Leap Year")
else:
    print(year,"is a Non Leap Year")
x=year%4
if x!=0:
    print("Previous Leap year:", year-x)
else:
    print("Next leap year:", input_year+4)
