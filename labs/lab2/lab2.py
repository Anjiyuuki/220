"""
Name: Angie-Bui
lab2.py

Problem: Ask user how many values they want to input, take input to compute averages
of three different math mean calculation: Arithmetic mean, Harmonic mean, and Geometric
mean.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

def means():
    num_vals = eval(input("Enter the number of values to be entered:"))
    rms_acc = 0
    harmon_acc = 0
    geo_acc = 1

    for average_mean in range(num_vals):
        calc_val = eval(input("Enter values:"))
        sq_of_val = calc_val ** 2
        rms_acc = rms_acc + sq_of_val
        harmon_acc = (1 / calc_val) + harmon_acc
        geo_acc = geo_acc * calc_val
    geo_acc = round(geo_acc ** (1/num_vals), 3)
    harmon_acc = round((num_vals / harmon_acc), 3)
    rms_acc = rms_acc/ num_vals
    rms_acc = round((rms_acc ** 0.5), 3)

    print("RMS Average=", rms_acc)
    print("Harmonic Mean=", harmon_acc)
    print("Geometric Mean=", geo_acc)

means()
