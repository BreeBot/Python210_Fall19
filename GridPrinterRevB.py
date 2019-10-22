#-------------------------------------------------#
# Title: Grid Printer
# Dev:   Breana K. Merriweather
# Date:  October 20, 2019
# ChangeLog: (Who, When, What)
#   BKM, 10/19/2019, Created Script

#-------------------------------------------------#

#-- Objective --#
#Write a function that draws a similar grid
#with a specified number of rows and columns,
#and with each cell a given size.

#-- Input/Output --#
#ask user how big the grid should be


greeting =print("You will be prompted to enter number of rows/columns and specified size")

#define a function for how how many rows/columns and unit size the grid should be
def print_grid(rowCol, unit):
    for _ in range(rowCol):
        print(("+" + "- " * unit) * rowCol + "+")
        for _ in range(unit):
            print(("|" + "  " * unit) * rowCol + "|")
    print(("+" + "- " * unit) * rowCol + "+")

rowCol=int(input("Rows/Columns: "))
unit=int(input("Unit: "))
print_grid(rowCol, unit)








    
