from graphics import Point, GraphWin, Text, Entry

def convert_gui():
    win = GraphWin("Convert", 700, 700)
    win.setCoords(0,0,10,10)
    celsius_txt = Text(Point(3,8),"Enter Celsius:")
    celsius_entry = Entry(Point(7,8), 10)
    click_text = Text(Point(5,5), "Click to Convert")
    result_text = Text(Point(5,1), "")

    celsius_txt.draw(win)
    celsius_entry.draw(win)
    click_text.draw(win)
    result_text.draw(win)
    win.getMouse()
    celsius_temp = eval(celsius_entry.getText())
    fah = celsius_temp * 9/5 +32
    result_text.setText(fah)
    win.getMouse()

convert_gui()