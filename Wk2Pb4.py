#!/usr/bin/env python3
"""
Problem 4 from Week 2 Exercises for MATH20621 - Programming with Python

The problem reads 'Solve the previous problem by taking multiple maximum digits
into account as many times as they appear (1777 adds 21 = 7 + 7 + 7 to the sum).'
"""
#initialise a counter
i = 0
#initialise the sum
d = 0
n = int(input("Input a natural number: >"))
#loop to ensure that n is natural (i.e. > 0)
while n <= 0:
    n = int(input("Try again: >"))
#get n integers to sum their maximum digit
for i in range(n):
    current = int(input("Input an integer: >"))
    max_digit = 0
    md_occurances = 0
    #to avoid working with negatives, make a new variable as |current|
    tmp = abs(current)
    #when tmp = 0, there are no more digits left
    while tmp != 0:
        #last digit is remainder when tmp is divided by 10
        r = tmp%10
        #check if r is actually the max digit and add on
        if r == max_digit:
            md_occurances += 1
        if r > max_digit:
            max_digit = r
            md_occurances = 1
        #remove the last digit and repeat
        tmp //= 10
    #add the maximum digit to the sum
    print("Adding " + str(md_occurances) + " lots of",max_digit)
    d += (max_digit * md_occurances)
print("Sum is:",d)
