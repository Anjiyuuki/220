"""
Name: Angie Bui
hw6.py

Problem: This programs deals with encoding and decoding, ceasar cipher.

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""
import math


def cash_converter():
    integer_value = float(input("Enter an integer:"))
    answer = "That is $ {:.2f}".format(integer_value)
    print(answer)


def encode():
    message = input("Enter a message:")
    key = eval(input("Enter a key:"))
    acc = ""
    for letter in message:
        num = ord(letter)
        add_key = num + key
        letter = chr(add_key)
        acc = acc + letter
    print(acc)


def sphere_area(radius):
    area = 4 * math.pi * (radius**2)
    return area


def sphere_volume(radius):
    vol = (4/3)*math.pi * (radius**3)
    return vol


def sum_n(number):
    num = (number*(number+1))/2
    return num


def sum_n_cubes(number):
    num = ((number**2)*(number+1)**2)/4
    return num


def encode_better():
    message = input("Enter a message:")
    key = input("Enter a key:")
    output = ""

    for i in range(len(message)):
        letter = ord(message[i]) - 65
        shift = ord(key[i % len(key)]) - 65
        new_value = letter + shift
        mod = new_value % 58
        convert = mod + 65
        new_word = chr(convert)
        output = output + new_word
    print(output)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    # encode_better()
    pass
 
