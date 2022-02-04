"""
Name: Angie Bui
hw3.py

Problem: These programs calculates different arithmetics with
user input and output. Applying the knowledge of for loops.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def average():
    grade_acc = 0
    number_grade = eval(input("How many grade will you enter?"))
    for num in range(number_grade):
        calc_val = eval(input("Enter Grade:"))
        grade_acc = grade_acc + calc_val
    grade_acc = grade_acc/number_grade
    print("Average is:", grade_acc)

def tip_jar():
    tip = 0
    for t in range(5):
        add_tip = eval(input("How much would you like to donate?"))
        tip = tip + add_tip
    print("Total tips:", tip)

def newton():
    num_to_sq = int(input("What number do you want to square root?"))
    approx = int(input("How many times should we improve the approximation?"))
    improv = num_to_sq
    for i in range(approx):
        answer = (improv+(num_to_sq/improv))/2
        improv = answer
    print("The square root is approximately:", answer)

def sequence():
    tms = eval(input("Enter how many terms you like?"))
    for i in range(1, tms+1):
        print((i - 1) + (i % 2), end=" ")

def pi():
    series = eval(input("How many terms in the series:"))
    total = 1
    top = 0
    bottom = 0
    for i in range(series):
        top = i + (2.0 - (i % 2.0))
        bottom = i + (1.0 + (i % 2.0))
        total *= top/bottom
    answer = total * 2
    print(answer)

if __name__ == '__main__':
    average()
    tip_jar()
    newton()
    sequence()
    pi()
