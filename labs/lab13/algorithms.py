"""
Name: Angie Bui
algorithms.py

Problem: Using While loops and decision structures.
Implmenting different sort methods. 

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


def selection_sort(values):
    for i in range(len(values)):
        lower = values[i]
        position = i
        for j in range(i + 1, len(values)):
            if values[j] < lower:
                lower = values[j]
                position = j
        values[i], values[position] = values[position], values[i]


def calc_area(rect):
    p1 = rect.getP1()
    p2 = rect.getP2()
    dx = abs(p1.getX() - p2.getX())
    dy = abs(p1.getY() - p2.getY())
    area = dx * dy
    return area


def rect_sort(rectangles):
    dic = {}
    areas = []
    for rect in rectangles:
        dic[calc_area(rect)] = rect
        areas.append(calc_area(rect))
    selection_sort(areas)
    for i in range(len(areas)):
        rectangles[i] = dic[areas[i]]

