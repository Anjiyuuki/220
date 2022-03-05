from graphics import *
import math

def sing(name, holiday):
    print("Happy {} Birthday to you".format(holiday))
    print("Happy {} Birthday to you".format(holiday))
    print("Happy Birthday dear {}".format(name))
    print("Happy {} Birthday to you".format(holiday))
sing("Yuuki", "Sweet 16")
sing("Emma", "Sweet 16")

def square(num):
    num_sq = num * num
    return num_sq
x = square(8)
print(x)

def distance(p1, p2):
    x1 = p1.getX()
    x2 = p2.getX()
    y1 = p1.getY()
    y2 = p2.getY()
    point_distance = math.sqrt((math.pow((x2-x1),2) + math.pow((y2-y1),2)))
    return point_distance
point_A = Point(2,3)
point_B = Point(100,200)
d = distance(point_A, point_B)
print(d)


def sum_diff(x,y):
    sum_value = x + y
    diff_value = x - y
    return sum_value, diff_value


my_sum, my_diff = sum_diff(10, 7)
print(my_sum, my_diff)

def get_discount(price, sale):
    price = price * (1 - sale)
    return price

price = 100
new_price = get_discount(price,.20)
print(new_price)


def change_point(p, x, y):
    p.move(x, y)

p1 = Point(2,3)
change_point(p1, 100, 200)

def change_point():
    p = Point(2,3)
    p.move(x, y)


my_point = Point(2,3)
print(my_point.getX(), my_point.getY())
change_point(my_point, 100, 200)
print(my_point.getX(), my_point.getY())

def double_list(list_one):
    for i in range(len(list_one)):
        list_one[i] = list_one[i] * 2

my_list = [ 1, 2, 3, 4, 5]
print(my_list)
double_list(my_list)
print(my_list)

def double_value(x):
    x = x * 2
    return x
my_value = 7
print(my_value)
y = double_value(my_value)
print(y)

