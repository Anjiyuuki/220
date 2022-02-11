"""
Name: Angie Bui
hw4.py

Problem: The first 3 programs utilizes the graphics library to
create a window and different objects. The last program approximate
the value of pie by summing the term of the series given.

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
from graphics import *
import math

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw Squares")
    instructions.draw(win)

    shape_width = 50
    shape_height = 50
    shape = Rectangle(Point(100, 100), Point(shape_width, shape_height))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    shape = Rectangle(Point(100, 100), Point(shape_width, shape_height))
    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        shape = Rectangle(Point(100, 100), Point(shape_width, shape_height))
        shape.setOutline("red")
        shape.setFill("red")
        shape.draw(win)
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape.move(change_x, change_y)
    close_msg = Point(width / 2, height / 2)
    close = Text(close_msg, "Click again to close")
    close.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)

    click = win.getMouse()
    click2 = win.getMouse()

    click_1x = click.getX()
    click_1y = click.getY()
    click_2x = click2.getX()
    click_2y = click2.getY()

    shape = Rectangle(Point(click_1x, click_1y), Point(click_2x, click_2y))
    shape.setOutline("Black")
    shape.setFill("Green")
    shape.draw(win)

    perimeter = 2*(click_2x + click_2y)
    area = click_2x * click_2y

    close_msg = Point(width / 2, height / 2)
    close = Text(close_msg, "Click again to close")
    close.draw(win)

    perim_display = Point(width / 2, height - 40)
    pm = "Perimeter:", perimeter
    perim_msg = Text(perim_display, pm)
    perim_msg.draw(win)
    area_loc = Point(width / 2, height - 20)
    ar = "Area:", area
    area_msg = Text(area_loc, ar)
    area_msg.draw(win)

    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Circle", width, height)

    click = win.getMouse()
    click2 = win.getMouse()

    click_x = click.getX()
    click_y = click.getY()
    click2_x = click2.getX()
    click2_y = click2.getY()
    center = Point(click_x, click_y)

    left = (click2_x - click_x)**2
    right = (click2_y - click_y)**2
    radius = (left+right)**(1/2)

    shape = Circle(center, radius)
    shape.setFill("Light Blue")
    shape.setOutline("Black")
    shape.draw(win)

    c_display = Point(width / 2, height - 40)
    c_r = "Radius:", radius
    cr_msg = Text(c_display, c_r)
    cr_msg.draw(win)

    close_msg = Point(width / 2, height / 2)
    close = Text(close_msg, "Click again to close")
    close.draw(win)

    win.getMouse()
    win.close()


def pi2():
    series = eval(input("Enter the number of terms to sum:"))
    acc = 0
    numer = 4
    denom = 1
    switch = 1
    for i in range(series):
        acc = acc + switch * (numer / denom)
        denom = denom + 2
        switch = switch * -1
    print("Pi approximation:", acc)
    print("Accuracy:", abs(math.pi-acc))


if __name__ == '__main__':
    squares()
    rectangle()
    circle()
    pi2()

    
