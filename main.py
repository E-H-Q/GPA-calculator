#!/bin/bash/python3

print ("Enter your grades, (percent): \n")

one = input ("1st class: ")
two = input ("2nd class: ")
three = input ("3rd class: ")
four = input ("4th class: ")
five = input ("5th class: ")
six = input ("6th class: ")
seven = input ("7th class: ")

one = one / 20 - 1
two = two / 20 - 1
three = three / 20 -1
four = four / 20 - 1
five = five / 20 - 1
six = six / 20 - 1
seven = seven / 20 - 1

total = one + two + three + four + five + six + seven
gpa = total / 7
print (round(gpa,1))
