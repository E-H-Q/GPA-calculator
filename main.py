#!/bin/bash/python3

per_num = int(input ("How many classes do you have?: "))
pers = [None] * per_num
i = 0

print ("\nEnter your grades, (percentages): ")

while (i < len(pers)):
    pers[i] = int(input ("  Period " + str(i+1) + ": ")) / 20 - 1
    i += 1

total = sum(pers)
gpa = total / (len(pers))
print ("\nGPA:",round(gpa,1))
