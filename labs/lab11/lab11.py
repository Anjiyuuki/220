"""
Name: Angie Bui
lab11.py

Problem: Uses the Door and Button class created to make different
objects and functionality.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from lab10.button import*
from lab10.door import*
from random import randint
from graphics import*

def three_door_game():
    win = GraphWin("Test", 900, 800)
    bak = win.setBackground("Blue")


    the_exit = Button(Rectangle(Point(700, 50), Point(850, 150)), "Exit")
    the_exit.color_button("light gray")
    the_exit.draw(win)

    door_1 = Door(Rectangle(Point(100, 200), Point(300, 699)), "Door 1")
    door_1.color_door("brown")
    door_1.draw(win)

    door_2 = Door(Rectangle(Point(340, 200), Point(540, 699)), "Door 2")
    door_2.color_door("brown")
    door_2.draw(win)

    door_3 = Door(Rectangle(Point(590, 200), Point(780, 699)), "Door 3")
    door_3.color_door("Brown")
    door_3.draw(win)

    win_rectangle_point_1 = Point(75, 50)
    win_rectangle_point_2 = Point(150, 125)
    win_box = Rectangle(win_rectangle_point_1, win_rectangle_point_2)
    win_box.draw(win)
    win_text = Text(Point(112.5, 40), 'Wins')
    win_text.draw(win)

    loss_rectangle_point_1 = Point(150, 50)
    loss_rectangle_point_2 = Point(225, 125)
    loss_box = Rectangle(loss_rectangle_point_1, loss_rectangle_point_2)
    loss_box.draw(win)
    loss_text = Text(Point(187.5, 40), 'Losses')
    loss_text.draw(win)



    again = Text(Point(450,750), "click anywhere to play again")
    winning_text = Text(Point(450,150), "You win!")


    random_door = randint(1, 3)

    if random_door == 1:
        door_1.set_secret(True)
    if random_door == 2:
        door_2.set_secret(True)
    if random_door == 3:
        door_3.set_secret(True)

    win_list = []
    lose_list = []

    pt = win.getMouse()

    win_number = Text(Point(112, 87), '')
    win_number.draw(win)
    win_number.setText(len(win_list))
    loss_number = Text(Point(187, 87), '')
    loss_number.draw(win)
    loss_number.setText(len(lose_list))


    while not the_exit.is_clicked(pt):
        secret_txt = Text(Point(450, 150), "I have a secret door")
        secret_txt.draw(win)
        click_to_guess = Text(Point(450, 750), "Click to guess which is the secret door!")
        click_to_guess.draw(win)
        door_1.color_door("brown")
        door_2.color_door("brown")
        door_3.color_door("brown")
        random_door = randint(1, 3)
        if random_door == 1:
            door_1.set_secret(True)
        if random_door == 2:
            door_2.set_secret(True)
        if random_door == 3:
            door_3.set_secret(True)

        if random_door == 1 and door_1.is_clicked(pt):
            door_1.color_door("green")
            secret_txt.undraw()
            winning_text.draw(win)
            click_to_guess.undraw()
            again.draw(win)
            win_list.append('w')
            win_number.setText(len(win_list))
            loss_number.setText(len(lose_list))
            winning_text.undraw()
            again.undraw()
        elif random_door == 2 and door_2.is_clicked(pt):
            door_2.color_door("green")
            secret_txt.undraw()
            winning_text.draw(win)
        elif random_door == 3 and door_3.is_clicked(pt):
            door_3.color_door("green")
            secret_txt.undraw()
            winning_text.draw(win)
        else:
            winning_text.undraw()
            if door_1.is_clicked(pt):
                door_1.color_door("pink")
                secret_txt.undraw()
                click_to_guess.undraw()
                winning_text.setText("sorry, incorrect!")
            elif door_2.is_clicked(pt):
                door_2.color_door("pink")
                secret_txt.undraw()
                click_to_guess.undraw()
                winning_text.setText("sorry, incorrect!")
            elif door_3.is_clicked(pt):
                door_3.color_door("pink")
                secret_txt.undraw()
                click_to_guess.undraw()
                winning_text.setText("sorry, incorrect!")

        pt = win.getMouse()

    win.close()
three_door_game()

