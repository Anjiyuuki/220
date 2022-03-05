"""
Name: Angie Bui
Lab7.py

Problem: This program utilizes the graphics package and deals with
decision statements (True/ False). The ball starts from a random
location and color and bounce back when hitting the sides or each other.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from random import randint
from time import sleep
import math
from graphics import *


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(circle_ball, circle_ball2):
    ball_center = circle_ball.getCenter()
    ball_x = ball_center.getX()
    ball_y = ball_center.getY()
    ball_radius = circle_ball.getRadius()

    ball2_center = circle_ball2.getCenter()
    ball2_x = ball2_center.getX()
    ball2_y = ball2_center.getY()
    ball2_radius = circle_ball2.getRadius()

    d = math.sqrt(((ball2_x- ball_x)**2) + ((ball2_y - ball_y)**2))
    radius_eq = ball_radius + ball2_radius

    if d <= radius_eq:
        return True
    else:
        return False


def hit_vertical(circle_ball, win):
    v_center = circle_ball.getCenter()
    v_y_pos = v_center.getY()
    v_radius = circle_ball.getRadius()
    v_height = win.getHeight()
    return v_y_pos <= v_radius or v_y_pos >= v_height - v_radius


def hit_horizontal(circle_ball, win):
    h_center = circle_ball.getCenter()
    h_x_pos = h_center.getX()
    h_radius = circle_ball.getRadius()
    h_width = win.getWidth()
    return h_x_pos <= h_radius or h_x_pos >= h_width - h_radius


def get_random_color(circle_ball):
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color

def bumper():
    width = 600
    height = 600
    win = GraphWin("Bumper", width, height)

    ball = Circle(Point(randint(1,600), randint(1,600)), 20)
    ball.setFill(get_random_color(ball))

    ball2 = Circle(Point(randint(1,600),randint(1,600)), 20)
    ball2.setFill(get_random_color(ball2))

    ball.draw(win)
    ball2.draw(win)

    ball_x_move = get_random(10)
    ball_y_move = get_random(10)
    ball2_x_move = get_random(10)
    ball2_y_move= get_random(10)

    while not win.checkMouse():
        ball.move(ball_x_move, ball_y_move)
        ball2.move(ball2_x_move, ball2_y_move)
        if did_collide(ball, ball2):
            ball_x_move = -ball_x_move
            ball_y_move = -ball_y_move
            ball2_x_move = -ball2_x_move
            ball2_y_move = -ball2_y_move
        if hit_horizontal(ball, win):
            ball_x_move = -ball_x_move

        if hit_horizontal(ball2, win):
            ball2_x_move = -ball2_x_move
          
        if hit_vertical(ball, win):

            ball_y_move = -ball_y_move
        if hit_vertical(ball2, win):
            
            ball2_y_move = -ball2_y_move
        sleep(0.01)

    win.close()

bumper()