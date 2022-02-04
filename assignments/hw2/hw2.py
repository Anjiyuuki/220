"""
Name: Angie Bui
hw2.py

Problem: This program solves sum of threes with user inputting upper bound, multiplication table,
calculating area of a triangle with input of 3 sides, sum square for lower to upper range, and
power input base and exponent.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    bound = eval(input("What is the upper bound?"))
    bound = bound + 1
    sum = 0
    for f in range(0, bound,3):
        sum = sum + f
    print("Sum of threes is:", sum)


def multiplication_table():
    for i in range(1,11):
        for j in range(1,11):
                print(i*j, end="\t ")
        print()

def triangle_area():
    side_a = eval(input("Enter side a length:"))
    side_b = eval(input("Enter side b length:"))
    side_c = eval(input("Enter side c length:"))

    s = (side_a + side_b + side_c)/2
    x = s*(s - side_a)*(s - side_b) * (s - side_c)
    area = math.sqrt(x)
    print("Area is:", area)

def sum_squares():
    sum= 0
    lower = eval(input("Enter lower range:"))
    upper = eval(input("Enter upper range:"))
    upper = upper + 1
    for square in range(lower, upper):
        pow = square * square
        sum = sum + pow
    print(sum)


def power():
    base = eval(input("Enter base:"))
    exponent = eval(input("Enter exponent:"))
    answer = int(math.pow(base, exponent))
    print(base,"^",exponent,"=",answer)


if __name__ == '__main__':
    sum_of_threes()
    multiplication_table()
    triangle_area()
    sum_squares()
    power()


