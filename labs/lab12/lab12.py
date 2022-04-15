"""
Name: Angie Bui
lab12.py

Problem: Using While loops and decision structures.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from random import*


def find_and_remove_first(my_list, val):
    i = 0
    while i < len(my_list):
        if my_list[i] == val:
            my_list.insert(i, 'Angie')
            my_list.pop(i + 1)
    i += 1


def good_input():
    guess = 0
    while guess < 1 or guess > 10:
        guess = eval(input("Guess a number: "))
        if guess > 10:
            print("Number too high.")
        elif guess < 1:
            print("Number is too low.")


def num_digits():
    num = eval(input("Enter a number: "))
    while num >= 1:
        digits = 0
        while num != 0:
            num = num // 10
            digits = digits + 1
        print("There are " + str(digits) + " digits.")
        num = eval(input("Enter a number: "))


def hi_lo_game():
    user_guess = eval(input("Guess a number:"))
    guess = 1
    random_number = randint(1,100)
    while user_guess != random_number and guess != 7:
        guess += 1
        if user_guess < random_number:
            print("too low")
        else:  # user_guess > random_number
            print("too high")
        user_guess = eval(input("guess the number: "))
        if user_guess == random_number:
            print("You won in " + str(guess) + " guesses!")
        if guess == 7:
            print("Sorry you lose. The number was " + str(random_number))
