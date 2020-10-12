#!/usr/bin/env python3
"""
Problem 2 from Week 2 Exercises for MATH20621 - Programming with Python

The problem reads 'Write a program that loads integers until a zero is loaded
and then prints the maximum among them and which one it was (not taking the zero
into account). If there is more than one maximum, use the first one among them
as a solution.'
"""
#initialise a counter
i = 0
current = int(input("Input an integer: >"))
#the first value is obviously going to be the maximum, so set maximum to that
#value
max_value = current
while current != 0:
    i += 1
    #when the new input is larger than the current max, change all details of
    #which number is the maximum and which index it was
    if current > max_value:
        max_value = current
        max_index = i
    current = int(input("Input an integer: >"))
#if only a 0 was inputted, there is no maximum to be found.
if i > 0:
    print("The maximum number is #" + str(max_index) + " and its value is",max_value)
else:
    print("No maximum was found.")
