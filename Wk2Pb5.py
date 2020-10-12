#!/usr/bin/env python3
"""
Problem 5 from Week 2 Exercises for MATH20621 - Programming with Python

The problem reads 'Write a program that inputs integers until it gets a zero and
print the one with the maximum sum of its odd digits. If there is more than one
such number, print the first one.'
"""
#initialise a counter
i = 0
#initialise the sum
d = 0
current = int(input("Input an integer: >"))
#the first value is obviously going to be the maximum, so set maximum to that
#value
int_with_max_sum = current
max_sum = 0
while current != 0:
    i += 1
    tmp = abs(current)
    #initialise the second sum
    odd_sum = 0
    #when tmp = 0, there are no more digits left
    while tmp != 0:
        #last digit is remainder when tmp is divided by 10, then check if odd
        r = tmp%10
        if r%2 != 0:
            odd_sum += r
        #remove the last digit and repeat
        tmp //= 10
    #change both the maximum sum and which integer has that sum if necessary
    if odd_sum > max_sum:
        max_sum = odd_sum
        int_with_max_sum = current
    current = int(input("Input an integer: >"))
if i > 0:
    print("The number with the maximum sum of odd digits is " + str(int_with_max_sum) +
          " and said sum is",max_sum)
else:
    print("No maximum was found.")
