from graphics import Rectangle, Circle, Polygon, Text, GraphWin, Point, Line
from time import sleep
"""
Name: Angie-Bui
lab4.py

Problem: This program utilizes the graphics library and loop to make a greeting card.
It has an arrow shooting through the heart using time.sleep. 

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def greeting_card():
    width = 700
    height = 700

    win = GraphWin("Greeting Card", width,height)
    win.setCoords(0,0,10,10)
    win.setBackground("Pink")

    left_circle = Circle(Point(4,7), 1)
    left_circle.setFill("Red")
    left_circle.setOutline("Red")

    right_circle = Circle(Point(5.5, 7), 1)
    right_circle.setFill("Red")
    right_circle.setOutline("Red")

    tri_bot = Polygon(Point(3,7),Point(6.5,7), Point(4.6,3.5))
    tri_bot.setFill("Red")
    tri_bot.setOutline("Red")

    writing = Text(Point(5,2),"Happy Valentine's Day!")
    writing.setSize(30)


    left_circle.draw(win)
    right_circle.draw(win)
    tri_bot.draw(win)
    writing.draw(win)

    arrow = Line(Point(0, 0), Point(2, 2))
    arrow.setWidth(4)
    arrow.setArrow("last")
    arrow.draw(win)


    for i in range(5):
        arrow.move(2,3)
        sleep(0.5)

    close_msg = Text(Point(5, 1), "Click anywhere to close.")
    close_msg.setSize(20)
    close_msg.draw(win)

    win.getMouse()
    win.close()
greeting_card()
