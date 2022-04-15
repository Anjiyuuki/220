from graphics import Entry, Point, GraphWin, Text


win = GraphWin("Smiley Face", 700,700)
win.setCoords(0,0,10,10)
label = Text(Point(5,1),"Your name")
user_input = Entry(Point(5,5), 10)
user_input.setText("Enter your name here")
user_input.draw(win)
win.getMouse()
name = user_input.getText()
label.setText(name)
win.getMouse()
