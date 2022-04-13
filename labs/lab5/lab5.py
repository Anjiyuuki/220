"""
Name: Angie Bui
lab5.py

Problem: These program incorporate the graphics library to make a triangle,
change shape color, and make a target. Also uses list and strings skills. 

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
from graphics import *
import math


def triange():
    width = 400
    height = 400
    win = GraphWin("Triangle", width, height)

    msg = Point(width / 2, 20)
    instruction = Text(msg, "Click 3 spot to make a triangle")
    instruction.draw(win)

    click = win.getMouse()
    click2 = win.getMouse()
    click3 = win.getMouse()

    click_1x = click.getX()
    click_1y = click.getY()
    click_2x = click2.getX()
    click_2y = click2.getY()
    click_3x = click3.getX()
    click_3y = click3.getY()

    shape = Polygon(Point(click_1x, click_1y), Point(click_2x, click_2y), Point(click_3x, click_3y))
    shape.setOutline("Black")
    shape.setFill("Green")
    shape.draw(win)

    # Length 1
    dx = click_2x - click_1x
    dy = click_2y - click_1y
    dxsq = dx ** 2
    dysq = dy ** 2
    length_one = math.sqrt((dxsq + dysq))

    # Length 2
    dx_two = click_3x - click_1x
    dy_two = click_3y - click_1y
    dxsq_two = dx_two ** 2
    dysq_two = dy_two ** 2
    length_two = math.sqrt((dxsq_two + dysq_two))

    # Length 3
    dx_three = click_2x - click_3x
    dy_three = click_2y - click_3y
    dxsq_three = dx_three ** 2
    dysq_three = dy_three ** 2
    length_three = math.sqrt((dxsq_three + dysq_three))

    # Perimeter Math Formula
    add_length = length_one + length_two + length_three
    s = add_length / 2

    # Area math formula
    subtract = (s - length_one)*(s - length_two)*(s - length_three)
    tm = s * subtract
    area = math.sqrt(tm)

    # Display Perimeter
    perim_display = Point(width / 2, height - 40)
    pm = "Perimeter:", s
    perim_msg = Text(perim_display, pm)
    perim_msg.draw(win)

    # Display Area
    area_location = Point(width / 2, height - 20)
    ar = "Area:", area
    area_msg = Text(area_location, ar)
    area_msg.draw(win)

    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    red_centerpoint = Point(220, win_height / 2 + 40)
    red_text_entry = Entry(red_centerpoint, 10)
    red_text_entry.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    green_centerpoint = Point(220, win_height / 2 + 70)
    green_text_entry = Entry(green_centerpoint, 10)
    green_text_entry.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    blue_centerpoint = Point(220, win_height / 2 + 100)
    blue_text_entry = Entry(blue_centerpoint, 10)
    blue_text_entry.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()

        red_number = red_text_entry.getText()
        r = eval(red_number)
        green_number = green_text_entry.getText()
        g = eval(green_number)
        blue_number = blue_text_entry.getText()
        b = eval(blue_number)
        shape.setFill(color_rgb(r, g, b))

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_string():
    word = input("Enter a string:")
    first_character = word[0]
    print(first_character)
    last_character = word[-1]
    print(last_character)
    position_two_five = word[1:5]
    print(position_two_five)
    con_last_first = first_character + last_character
    print(con_last_first)
    first_three_repeat = word[0:3]
    for i in range(10):
        print(first_three_repeat)
    for i in word:
        print(i)
    num_character = len(word)
    print(num_character)


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    # 1
    x = values[1] + values[3]
    print(x)
    # 2
    x = values[0] + values[2]
    print(x)
    # 3
    x = values[1] * 7
    print(x)
    # 4
    x = [values[2], values[3], values[4]]
    print(x)
    # 5
    x = [values[2], values[3], values[0]]
    print(x)
    # 6
    x = [values[2], values[0], float(values[5])]
    print(x)
    # 7
    x = values[0] + values[2] + float(values[5])
    print(x)
    # 8
    x = len(values)
    print(x)


def another_series():
    num_series = eval(input("Enter the number of terms:"))
    accumulator = 0
    for i in range(num_series):
        calc = 2 + 2*(i % 3)
        accumulator = accumulator + calc
        print(calc, end=" ")

    print("\n" "sum =",accumulator)


def target():
    width = 400
    height = 400
    win = GraphWin("Target", width, height)

    center = Point(200,200)

    white_ring = Circle(center, 200)
    white_ring.setFill("White")
    white_ring.draw(win)

    black_ring = Circle(center, 160)
    black_ring.setFill("Black")
    black_ring.draw(win)

    blue_ring = Circle(center, 120)
    blue_ring.setFill("Blue")
    blue_ring.draw(win)

    red_ring = Circle(center, 80)
    red_ring.setFill("Red")
    red_ring.draw(win)

    yellow_ring = Circle(center, 40)
    yellow_ring.setFill("Yellow")
    yellow_ring.draw(win)

    close_msg = Point(width / 2, height / 2)
    close = Text(close_msg, "Click again to close")
    close.draw(win)

    win.getMouse()
    win.close()


triange()
color_shape()
process_string()
process_list()
another_series()
target()
