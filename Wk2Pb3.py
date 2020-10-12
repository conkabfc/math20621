#!/usr/bin/env python3
"""
Problem 3 from Week 2 Exercises for MATH20621 - Programming with Python

The problem reads 'Write a program that loads a natural number (a non-negative
integer) n and then loads n integers. The program has to print the sum of the
maximum digits of all the loaded numbers. If a number has multiple maximum
digits, they are still taken into the sum only once (1777 only adds 7 to the
sum, not 7 + 7 + 7).'
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
    #to avoid working with negatives, make a new variable as |current|
    tmp = abs(current)
    #when tmp = 0, there are no more digits left
    while tmp != 0:
        #last digit is remainder when tmp is divided by 10
        r = tmp%10
        #check if r is actually the max digit and add on
        if r > max_digit:
            max_digit = r
        #remove the last digit and repeat
        tmp //= 10
    #add the maximum digit to the sum
    d += max_digit
print("Sum is:",d)
