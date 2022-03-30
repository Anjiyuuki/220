"""
Name: Angie Bui
lab10.py

Problem: Uses the Door and Button class created to make different
objects and functionality.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import*
from button import*
from door import*


def main():
    win = GraphWin("Test", 700, 700)
    the_exit = Button(Rectangle(Point(200,50),Point(500,200)), "Exit")
    the_exit.color_button("light gray")
    the_exit.draw(win)

    the_door = Door(Rectangle(Point(200, 250), Point(500, 699)), "Closed")
    the_door.color_door("red")
    the_door.draw(win)

    pt = win.getMouse()
    while not the_exit.is_clicked(pt):
        if the_door.is_clicked(pt) and the_door.get_label() == "Open":
            the_door.close("red", "Closed")
        else:
            the_door.open("white", "Open")
        pt = win.getMouse()

    win.close()

main()
