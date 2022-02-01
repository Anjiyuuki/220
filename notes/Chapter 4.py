import graphics
# from graphics import Point, GraphWin
my_point = graphics.Point(50,70)
point_a = graphics.Point(70,90)

print(my_point.getX())  # .getX()   accessor methods
print(point_a.getX())

point_a.move(10,0)
print(point_a.getX())


window = graphics.GraphWin("CSCI 220", 700, 700)
middle = graphics.Point(350, 350)
middle.draw(window)


my_circle = graphics.Circle(middle, 40)
my_circle.draw(window)
input('hit enter to close')

