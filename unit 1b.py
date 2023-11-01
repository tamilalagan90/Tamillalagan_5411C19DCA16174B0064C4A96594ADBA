#program to whether the year is leap or not

year=int(input("Enter year of your choice:"))

if(year%4==0 and year%100!=0 or year%400==0):
    print(f"The {year} is a leap year")
else:
    print(f"The {year} is not a leap year")