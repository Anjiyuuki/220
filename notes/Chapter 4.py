import graphics
# # from graphics import Point, GraphWin, Circle
# my_point = graphics.Point(50,70)
# point_a = graphics.Point(70,90)
#
# print(my_point.getX())  # .getX()   accessor methods
# print(point_a.getX())
#
# point_a.move(10,0)
# print(point_a.getX())
#
#
# window = graphics.GraphWin("CSCI 220", 700, 700)
# middle = graphics.Point(350, 350)
# middle.draw(window)
#
#
# my_circle = graphics.Circle(middle, 40)
# my_circle.draw(window)
# input('hit enter to close')


win = graphics.GraphWin("Smiley Face", 700,700)
win.setCoords(0,0,10,10)

face_center_point = graphics.Point(350,100)
face = graphics.Circle(face_center_point,100)
face.draw(win)

left_eye = graphics.Circle(graphics.Point(325,60),20)
left_eye.setFill('turquoise')
left_eye.setOutline('red')
#right_eye = graphics.Circle(graphics.Point(375,60),20)
right_eye = left_eye.clone()
right_eye.move(50,0)

# left_eye.setFill('turquoise')
# left_eye.setOutline('red')

#right_eye.setFill('turquoise')
#right_eye.setOutline('red')

text_point = graphics.Point(5,5)
label = graphics.Text(text_point, "Angie")


left_eye.draw(win)
right_eye.draw(win)
label.draw(win)

for i in range(1):
    click_point= win.getMouse()
    click_point.draw(win)
win.getMouse()


