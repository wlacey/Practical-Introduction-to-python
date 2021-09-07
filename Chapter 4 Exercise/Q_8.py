"""A year is a leap year if it is divisible by 4, except that years divisible by 100 are not leap years
unless they are also divisible by 400. Write a program that asks the user for a year and prints
out whether it is a leap year or not."""

year = int(input("Enter Year To Check if its a leap year: "))

if year % 4 == 0 or year % 100 != 0 and year % 400 == 0:

    print(year," Is a leap year")

else:
    print(year,"Is not a leap Year")

# I believe the following is the proper logic for the problem...
year = eval(input('Enter a year: '))
if (year % 4 == 0 and (not(year % 100 == 0))) or year % 400 == 0:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
