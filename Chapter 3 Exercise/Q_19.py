""""Write a program that draws “modular rectangles” like the ones below. The user specifies the
width and height of the rectangle, and the entries start at 0 and increase typewriter fashion
from left to right and top to bottom, but are all done mod 10. Below are examples of a 3  5
rectangle and a 4  8.
0 1 2 3 4
5 6 7 8 9
0 1 2 3 4

0 1 2 3 4 5 6 7
8 9 0 1 2 3 4 5
6 7 8 9 0 1 2 3
4 5 6 7 8 9 0 1"""

width = eval(input('Enter the width: '))
height = eval(input('Enter the height: '))
num = 0 # This count is for numbers in the matrix.
for i in range(height):
    count = 0 # Resets the count.
    print(sep = "") # Will force the numbers to continue on next line.
    while count < width: # While loop needed to create the width.
        print(num%10, end = ' ') # Mod 10 needed to create a loop from 0 to 9 with an ongoing increased count.
        num+=1
        count+=1
