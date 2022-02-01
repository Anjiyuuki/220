"""
Name: Angie-Bui
lab3.py

Problem: This program is used to find average number of vehicles that travel each
road per day and the overall number and average number of vehicles that have traveled
over all roads.User will input number of roads surveyed, days road surveyed, car traveled
per those days.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
def traffic():
    roads_surveyed = eval(input("How many roads were surveyed?"))

    cars_acc_total = 0

    for days in range(roads_surveyed):
        cars_acc = 0
        print("How many days was road", days + 1, "surveyed?")
        day_num = eval(input(""))
        for rd in range(day_num):
            print("How many cars traveled on day", rd + 1, "?")
            cars_day = eval(input(""))
            cars_acc_total = cars_acc_total + cars_day
            cars_acc = cars_acc + cars_day
        cars_average = cars_acc/day_num
        print("Road",days + 1, "average vehicles per day:",cars_average)

    print("Total number of vehicles traveled on all roads:", cars_acc_total)
    print("Average number of vehicles per road:",cars_acc_total/roads_surveyed)

traffic()