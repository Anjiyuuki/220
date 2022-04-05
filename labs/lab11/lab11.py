"""
Name: Angie Bui
lab11.py

Problem: Using button and door classes to create a three door game.
Game keep tracks of correct and incorrect guesses. 

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from lab10.door import*
from lab10.button import*
from random import*
from graphics import*


def three_door_game():
    # Graphics Window
    win = GraphWin('Three Door Game', 700, 700)
    win.setBackground('blueviolet')
    # Button and Door
    button = Button(Rectangle(Point(500, 25), Point(650, 100)), "Quit")
    door_1 = Door((Rectangle(Point(75, 200), Point(225, 600))), "Door 1")
    door_2 = Door((Rectangle(Point(275, 200), Point(425, 600))), "Door 2")
    door_3 = Door((Rectangle(Point(475, 200), Point(625, 600))), "Door 3")
    button.draw(win)
    door_1.draw(win)
    door_2.draw(win)
    door_3.draw(win)

    # Beginning color
    button.color_button("gray")
    door_1.color_door('chocolate4')
    door_2.color_door('chocolate4')
    door_3.color_door('chocolate4')


    random_door = randint(1, 3)
    if random_door == 1:
        door_1.set_secret(True)
    if random_door == 2:
        door_2.set_secret(True)
    if random_door == 3:
        door_3.set_secret(True)

    # Win and Lose Lists
    win_list = []
    lose_list = []
  
    win_box = Rectangle(Point(75, 50), Point(150, 125))
    win_box.draw(win)
    win_text = Text(Point(112, 40), 'Wins')
    win_text.draw(win)

    loss_box = Rectangle(Point(150, 50), Point(225, 125))
    loss_box.draw(win)
    loss_text = Text(Point(187, 40), 'Losses')
    loss_text.draw(win)

    click = Point(0, 0)
    win_number = Text(Point(112, 87), '')
    win_number.draw(win)
    win_number.setText(len(win_list))
    loss_number = Text(Point(187, 87), '')
    loss_number.draw(win)
    loss_number.setText(len(lose_list))
    while not button.is_clicked(click):
        secret_txt = Text(Point(350, 125), 'I have a secret door')
        secret_txt.draw(win)
        click_to_guess = Text(Point(350, 625), 'Click to guess which is the secret door!')
        click_to_guess.draw(win)
        click = win.getMouse()
        if door_1.is_clicked(click):
            if door_1.is_secret():
                door_1.color_door('aquamarine1')
                secret_txt.undraw()
                winning_text = Text(Point(350, 125), 'You Win!')
                winning_text.draw(win)
                click_to_guess.undraw()
                play_again = Text(Point(350, 625), 'Click anywhere to play again')
                play_again.draw(win)
                win_list.append('w')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                winning_text.undraw()
                play_again.undraw()
            else:
                door_1.color_door('pink')
                if door_2.is_secret():
                    door_2.color_door('aquamarine1')
                if door_3.is_secret():
                    door_3.color_door('aquamarine1')
                secret_txt.undraw()
                losing_txt = Text(Point(350, 125), 'Sorry, incorrect!')
                losing_txt.draw(win)
                click_to_guess.undraw()
                play_again = Text(Point(350, 625), 'Click anywhere to play again')
                play_again.draw(win)
                lose_list.append('l')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                losing_txt.undraw()
                play_again.undraw()

        elif door_2.is_clicked(click):
            if door_2.is_secret():
                door_2.color_door('aquamarine1')
                secret_txt.undraw()
                winning_text = Text(Point(350, 125), 'You Win!')
                winning_text.draw(win)
                click_to_guess.undraw()
                play_again = Text(Point(350, 625), 'Click anywhere to play again')
                play_again.draw(win)
                win_list.append('w')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                winning_text.undraw()
                play_again.undraw()
            else:
                door_2.color_door('pink')
                if door_1.is_secret():
                    door_1.color_door('aquamarine1')
                if door_3.is_secret():
                    door_3.color_door('aquamarine1')
                secret_txt.undraw()
                losing_txt = Text(Point(350, 125), 'Sorry, incorrect!')
                losing_txt.draw(win)
                click_to_guess.undraw()
                play_again = Text(Point(350, 625), 'Click anywhere to play again')
                play_again.draw(win)
                lose_list.append('l')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                losing_txt.undraw()
                play_again.undraw()

        elif door_3.is_clicked(click):
            if door_3.is_secret():
                door_3.color_door('aquamarine1')
                secret_txt.undraw()
                winning_text = Text(Point(350, 125), 'You Win!')
                winning_text.draw(win)
                click_to_guess.undraw()
                play_again = Text(Point(350, 625), 'Click anywhere to play again')
                play_again.draw(win)
                win_list.append('w')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                winning_text.undraw()
                play_again.undraw()
            else:
                door_3.color_door('pink')
                if door_1.is_secret():
                    door_1.color_door('aquamarine1')
                if door_2.is_secret():
                    door_2.color_door('aquamarine1')
                secret_txt.undraw()
                losing_txt = Text(Point(350, 125), 'Sorry, incorrect!')
                losing_txt.draw(win)
                click_to_guess.undraw()
                play_again = Text(Point(350, 625), 'Click anywhere to play again')
                play_again.draw(win)
                lose_list.append('l')
                win_number.setText(len(win_list))
                loss_number.setText(len(lose_list))
                click = win.getMouse()
                losing_txt.undraw()
                play_again.undraw()
        elif (not door_1.is_clicked(click)) and (not door_2.is_clicked(click)) and (not door_3.is_clicked(click)):
            secret_txt.undraw()
            click_to_guess.undraw()
        # Resets to beginning defaults
        door_1.color_door('chocolate4')
        door_2.color_door('chocolate4')
        door_3.color_door('chocolate4')
        door_1.set_secret(False)
        door_2.set_secret(False)
        door_3.set_secret(False)
        random_door = randint(1, 3)
        if random_door == 1:
            door_1.set_secret(True)
        if random_door == 2:
            door_2.set_secret(True)
        if random_door == 3:
            door_3.set_secret(True)

    win.close()

three_door_game()
