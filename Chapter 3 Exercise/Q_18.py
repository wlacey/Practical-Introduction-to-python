""""18. Write a program that given an amount of change less than $1.00 will print out exactly how
many quarters, dimes, nickels, and pennies will be needed to efficiently make that change.
[Hint: the // operator may be useful.]"""

##To fully understand this problem you have to understand what are the differences between quaters ,dimes ,nickels and pennies.
import sys

""" Quater = 25cents
    Dimes = 10cents
    Nickel = 5cents
    Penny = 1cent
    
"""


number = eval(input("Enter a number beween 0-99: "))
if number < 0 or number > 99:
    print("You entered a number in the wrong range!!!!!")
    sys.exit()

else:
      Quater = number // 25
      Dimes = number // 10
      Nickel = number // 5
      Penny = number // 1

print("Quater = ",Quater, "Dimes = ", Dimes, "Nickel = ", Nickel, "Penny = ", Penny)

# The following is a different approach...
pennies = 0
nickels = 0
dimes = 0
quarters = 0
change = eval(input('Enter the amount of change as a whole number: '))
while 1 > change or 99 < change:
    change = (input('Enter the amount of change as a whole number: '))
    continue
for i in range(change):
    pennies+=1
    if pennies == 5:
        pennies = 0
        nickels+=1
    if nickels == 2:
        nickels = 0
        dimes+=1
    if dimes == 2 and nickels == 1:
        dimes = 0
        nickels = 0
        quarters+=1
cents = round(change/100, 2)
print(f'Your change was {cents}. This will include {pennies} pennies, {nickels} nickels, {dimes} dimes, and {quarters} quarters.')
# Range can only use integers, not floats.
# So either take in integers or install numPy and import numpy module and call the arrange function.
