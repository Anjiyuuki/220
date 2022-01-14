"""
Name: Angie-Bui
Homework1.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length:"))
    width = eval(input("Enter the width:"))
    height = eval(input("Enter the height"))
    volume = length * width * height
    print("Volume=", volume)


def shooting_percentage():
    totalshot = eval(input("Enter the player's total shot:"))
    madeshot = eval(input("Enter how many shots the player made:"))
    percent = madeshot / totalshot * 100
    print("Shooting Percentage:", percent,"%")




def coffee():
    question = eval(input("How many pounds of coffee would you like?"))
    cost = question * 10.50
    shipping = question * 0.86
    total = cost + shipping + 1.50
    print("Your total is: $",total)


def kilometers_to_miles():
    travelled = eval(input("How many kilometers did you travel?"))
    convert = travelled * 0.6213
    miles = float(int(convert))
    print("That's",miles,"miles!")


if __name__ == '__main__':
    pass
