"""
Name: Angie Bui
lab6.py

Problem: Utilizes the concept of Caesar Cipher however shifts
the message based on provided keyword.

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
from graphics import *


def vigenere():
    width = 600
    height = 400
    win = GraphWin("Vigenere", width, height)

    # Message view and entry box
    msg_view = "Message to code:"
    inst = Text(Point(75, 75), msg_view)
    inst.draw(win)
    msg_entry = Entry(Point(250,75), 30)
    msg_entry.draw(win)

    # Keyword view and entry box
    keyword = "Enter Keyword:"
    kw = Text(Point(75, 150), keyword)
    kw.draw(win)
    key_entry = Entry(Point(250, 150), 30)
    key_entry.draw(win)

    # Rectangle Encode Button
    shape = Rectangle(Point(200,240),Point(375,190))
    shape.draw(win)
    msg_encode = "Encode"
    msg_encode_location = Text(Point(285,215),msg_encode)
    msg_encode_location.draw(win)

    # Click Button
    win.getMouse()

    # get text for entry box for string and keyword
    msg_string = msg_entry.getText()
    code = key_entry.getText()

    # Everything uppercase and no space
    up = msg_string.upper()
    string_combined = "".join(up.split(" "))
    up_key = code.upper()
    code_combined = "".join(up_key.split(" "))

    # Empty string
    output = ""

    for i in range(len(string_combined)):
        msg_code = ord(string_combined[i]) - 65
        shift_amount = ord(code_combined[i % len(code_combined)]) - 65
        new_value = msg_code + shift_amount
        # stays within the range of the alphabet
        letter_in_range_of_alphabet = new_value % 26
        secret = chr(letter_in_range_of_alphabet + 65)
        output = output + secret

    # delete rec box and msg
    msg_encode_location.undraw()
    shape.undraw()

    # Result
    result_msg = "Resulting Message: "
    result_location = Text(Point(width/2,250), result_msg)
    result_location.draw(win)

    result_out = output
    result_location = Text(Point(width/2, 290), result_out)
    result_location.draw(win)

    # Close
    close_msg = Point(width / 2, 390)
    close = Text(close_msg, "Click again to close")
    close.draw(win)

    win.getMouse()
    win.close()

vigenere()