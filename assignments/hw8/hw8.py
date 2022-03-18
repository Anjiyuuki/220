"""
Name: Angie Bui
hw8.py

Problem: Using if/elif/else statement and returning.  

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import*
import math


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2
    return nums


def sum_list(nums):
    acc = 0
    for i in range(len(nums)):
        acc = nums[i] + acc
    return acc


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    list_value = []
    for i in range(len(nums)):
        set_num_split = nums[i].split(', ')
        to_numbers(set_num_split)
        square_each(set_num_split)
        value = sum_list(set_num_split)
        list_value.append(value)
    return list_value


def starter(weight, wins):
    if 150 <= weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)

    center_two = win.getMouse()
    circumference_point_two = win.getMouse()
    radius_two = math.sqrt(
        (center_two.getX() - circumference_point_two.getX()) ** 2 +
        (center_two.getY() - circumference_point_two.getY()) ** 2)
    circle_two = Circle(center_two, radius_two)
    circle_two.setFill("light green")
    circle_two.draw(win)

    overlap_message = Text(Point(5, 4), "The circles overlap.")
    not_overlap_message = Text(Point(5, 4), "The circles do not overlap.")
    closing_message = Text(Point(5, 3), "Click again to close.")

    if did_overlap(circle_one, circle_two):
        overlap_message.draw(win)
        closing_message.draw(win)
    else:
        not_overlap_message.draw(win)
        closing_message.draw(win)

    win.getMouse()


def did_overlap(circle_one, circle_two):
    center_one = circle_one.getCenter()
    p1x = center_one.getX()
    p1y = center_one.getY()

    center_two = circle_two.getCenter()
    p2x = center_two.getX()
    p2y = center_two.getY()

    rad1 = circle_one.getRadius()
    rad2 = circle_two.getRadius()

    distance = ((p2x - p1x) ** 2 + (p2y - p1y) ** 2) ** (1 / 2)
    if distance <= rad1 + rad2:
        print("The circles overlap.")
        return True
    else:
        print("The circles do not overlap.")
        return False


if __name__ == '__main__':
    pass
