#!/bin/bash/python3

print ("Enter your grades, (percent): \n")

one = int(input ("1st class: "))
two = int(input ("2nd class: "))
three = int(input ("3rd class: "))
four = int(input ("4th class: "))
five = int(input ("5th class: "))
six = int(input ("6th class: "))
seven = int(input ("7th class: "))

one /= (20 - 1)
two /= (20 - 1)
three /= (20 -1)
four /= (20 - 1)
five /= (20 - 1)
six /= (20 - 1)
seven /= (20 - 1)

total = one + two + three + four + five + six + seven
gpa = total / 7
print (round(gpa,1))
