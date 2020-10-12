#!/usr/bin/env python3
"""
Problem 1 from Week 2 Exercises for MATH20621 - Programming with Python

The problem reads 'Write a program that loads one integer and prints the sum of
its odd digits. The output has to be in the form "The sum of the odd digits in
number n is d."'
"""
n = int(input("Input number n: >"))
#to avoid working with negatives, make a new variable as |n|
tmp = abs(n)
#initialise the sum
d = 0
#when tmp = 0, there are no more digits left
while tmp != 0:
    #last digit is remainder when tmp is divided by 10, then check if odd
    r = tmp%10
    if r%2 != 0:
        d += r
    #remove the last digit and repeat
    tmp //= 10
print("The sum of the odd digits in number " + str(n) + " is",d)
