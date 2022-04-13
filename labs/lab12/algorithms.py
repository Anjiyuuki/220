"""
Name: Angie Bui
lab12.py

Problem: Using While loops and decision structures.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def read_data(file_name):
    i = 0
    the_list = []
    open_file = open(file_name, "r")
    line = open_file.read()
    words = line.split()
    while i < len(words):
        nums = eval(words[i])
        the_list.append(nums)
        i += 1
    open_file.close()
    return the_list


def is_in_linear(search_val, values):
    i = 0
    while i < len(values):
        if search_val in values:
            return True
        else:
            return False
    i = i + 1





