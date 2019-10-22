#-------------------------------------------------#
# Title: FizzBuzz
# Dev:   Breana K. Merriweather
# Date:  October 20, 2019
# ChangeLog: (Who, When, What)
#   BKM, 10/19/2019, Created Script

#-------------------------------------------------#

#-- Objective --#
#Write a program that prints the numbers from 1 to 100 inclusive.
#But for multiples of three print “Fizz” instead of the number.
#For the multiples of five print “Buzz” instead of the number.
#For numbers which are multiples of both three and five print “FizzBuzz” instead


#Title
print("FizzBuzz!" *5)
for x in range(1, 101):
     if (x%3 == 0 and x%5 == 0):
         print("FizzBuzz")
     elif x%3 == 0:
         print("Fizz")
     elif x%5 == 0:
         print("Buzz")
     else:
         print(x, end=" \n")
    








    
