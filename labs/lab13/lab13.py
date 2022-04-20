"""
Name: Angie Bui
lab13.py

Problem: Option 1 Capstone, read data in file and give 
trade alert.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def trade_alert(file_name):
    in_file = open(file_name, "r")
    line = in_file.read()
    word = line.split()
    for num in range(len(word)):
        if eval(word[num]) > 830:
            location = num + 1
            print("Warning! Volume exceeds 830 at " + str(location) + " seconds!")
        elif eval(word[num]) == 500:
            location = num + 1
            print("Pay attention! Volume is equal to 500 at " + str(location) + " seconds!")
    in_file.close()

