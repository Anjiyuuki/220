"""
Name: Angie Bui
hw9.py

Problem: Create the hangman game. Using graphic library
and other functions

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import*
from graphics import*

def get_words(file_name):
    in_file = open(file_name, "r")
    contents_in_file = in_file.readlines()
    the_list = []
    for line in contents_in_file:
        the_list.append(line)
    return the_list


def get_random_word(words):
    ran_word = randint(0, len(words)-1)
    gotten_word = words[ran_word]
    secret_word = gotten_word.rstrip()
    return secret_word


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    word_collect = []
    for i in secret_word:
        if i not in guesses:
            word_collect.append('_')
        else:
            word_collect.append(i)
    guesser = ' '.join(word_collect)
    return guesser


def won(guessed):
    for letter in guessed:
        if '_' not in guessed:
            return True
        else:
            return False

def play_graphics(secret_word):

    win_width = 550
    win_height = 550
    win = GraphWin("Hangman", win_width, win_height)
    win.setBackground("white")

    # HangMan Body Parts
    ground_pt1 = Point(win_width / 2 - 100, 400)
    ground_pt2 = Point(win_width / 2 + 50, 400)
    ground = Line(ground_pt1, ground_pt2)
    ground.draw(win)
    v_pole = Point(win_width / 2, 400)
    v_p2 = Point(win_width / 2, 50)
    vert_pole = Line(v_pole, v_p2)
    vert_pole.draw(win)
    hp = v_p2.clone()
    hp2 = Point(win_width / 2 - 100, 50)
    h_pole = Line(hp, hp2)
    h_pole.draw(win)
    rope_top = hp2.clone()
    rope_bot = Point(win_width / 2 - 100, 100)
    rope_pole = Line(rope_top, rope_bot)
    rope_pole.draw(win)
    head_center = Point(win_width / 2 - 100, 125)
    head = Circle(head_center, 25)
    body_pt1 = Point(win_width / 2 - 100, 150)
    body_pt2 = Point(win_width / 2 - 100, 250)
    body = Line(body_pt1, body_pt2)
    right_leg_pt1 = body_pt2.clone()
    right_leg_pt2 = Point(win_width / 2 - 50, 300)
    right_leg = Line(right_leg_pt1, right_leg_pt2)
    left_leg_pt1 = right_leg_pt1.clone()
    left_leg_pt2 = Point(win_width / 2 - 150, 300)
    left_leg = Line(left_leg_pt1, left_leg_pt2)
    right_arm_pt1 = Point(win_width / 2 - 100, 200)
    right_arm_pt2 = Point(win_width / 2 - 150, 225)
    right_arm = Line(right_arm_pt1, right_arm_pt2)
    left_arm_pt1 = right_arm_pt1.clone()
    left_arm_pt2 = Point(win_width / 2 - 50, 225)
    left_arm = Line(left_arm_pt1, left_arm_pt2)

    guess_prompt_pt = Point(win_width / 2 - 75, win_height - 75)
    guess_prompt = Text(guess_prompt_pt, "Guess a letter:")
    guess_prompt.draw(win)

    # The word that was guessed - to the side of the screen
    incorrect_str = ""
    guessed_incorrect_pt = Point(450, win_height / 2 - 100)
    guessed_incorrect = Text(guessed_incorrect_pt, incorrect_str)
    guessed_incorrect.draw(win)

    # Type the word here
    entry_box = Point(win_width / 2, win_height - 75)
    guess_entry = Entry(entry_box, 4)
    guess_entry.draw(win)

    guesses_lst = []
    guesses_remain = 6
    guessed_correct = make_hidden_secret(secret_word, guesses_lst)
    guessed_correct_txt_pt = Point(win_width / 2 - 75, win_height - 100)
    guessed_correct_txt = Text(guessed_correct_txt_pt, guessed_correct)
    guessed_correct_txt.draw(win)
    while guesses_remain >= 0 and not guessed_correct == secret_word:
        # while not won or lost, loop
        win.getKey()
        # stop for keyboard input
        curr_guess = guess_entry.getText()
        # gets entry value at time of key input
        guess_entry.setText("")
        guesses_lst.append(curr_guess)
        if letter_in_secret_word(curr_guess, secret_word):
            # correctly guessed letter
            guessed_correct = make_hidden_secret(secret_word, guesses_lst)
            guessed_correct_txt.undraw()
            guessed_correct_txt = Text(guessed_correct_txt_pt, guessed_correct)
            guessed_correct_txt.draw(win)
        else:  # incorrect letter
            guesses_remain -= 1
            incorrect_str += curr_guess + " "
            guessed_incorrect.undraw()
            guessed_incorrect = Text(guessed_incorrect_pt, incorrect_str)
            guessed_incorrect.draw(win)
            if guesses_remain == 5:
                head.draw(win)
            elif guesses_remain == 4:
                body.draw(win)
            elif guesses_remain == 3:
                right_leg.draw(win)
            elif guesses_remain == 2:
                left_leg.draw(win)
            elif guesses_remain == 1:
                right_arm.draw(win)
            elif guesses_remain == 0:
                left_arm.draw(win)

        if guessed_correct.split(" ") == list(secret_word):
            end_pt = Point(win_width / 2, 25)
            end = Text(end_pt, "Winner!")
            end.draw(win)
            win.getMouse()
            break
        elif guesses_remain == 0:
            end_pt = Point(win_width / 2, 25)
            sorry_str = "Sorry, you lost.\n the word was " + secret_word
            end = Text(end_pt, sorry_str)
            end.draw(win)
            win.getMouse()
            break


def play_command_line(secret_word):
    guesses_lst = []
    guesses_remain = 6
    guessed_correct = make_hidden_secret(secret_word, guesses_lst)
    while guesses_remain >= 0 and not guessed_correct == secret_word:
        print("Already guessed:", guesses_lst)
        print("Guesses remaining:", guesses_remain)
        print(guessed_correct)
        curr_guess = input("Guess a letter: ")
        guesses_lst.append(curr_guess)
        if letter_in_secret_word(curr_guess, secret_word):
            guessed_correct = make_hidden_secret(secret_word, guesses_lst)
        else:
            guesses_remain -= 1
        if guessed_correct.split(" ") == list(secret_word):
            print("Winner!\n" + guessed_correct)
            break
        elif guesses_remain == 0:
            print("Sorry, you did not guess the word.")
            print("The secret word was " + secret_word)
        else:
            print()

if __name__ == '__main__':
    pass
    # play_command_line(secret_word)
    play_graphics('Hello')
