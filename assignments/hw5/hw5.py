"""
Name: Angie Bui
hw5.py

Problem: Practicing using different strings and list.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def name_reverse():
    name = input("Enter a name (first last):")
    name.split(' ')
    first, last = name.split(' ')
    ' '.join([last, first])
    finish = last + ', ' + first
    print(finish)


def company_name():
    domain = input("Enter a domain:")
    domain = domain.split('.')
    finish = domain[1]
    print(finish)


def initials():
    a = []
    amount = eval(input("How many students are in the class?"))
    # print("What is the name of student", i + 1, "?")
    for i in range(amount):
        name = input("What is the name of student" + str(i + 1) + "?")
        a.append(name)
        split = name.split()
        print(split[0][0] + split[1][0])
        a.clear()


def names():
    mylist = []
    string = ' '
    name = (input("Enter a list of names:"))
    l = name.split()
    # 0 ,   len(l) count number
    for x in range(0, len(l)):
        first = l[x][0]
        mylist.append(first)
    for i in range(0, len(mylist), 2):
        k = i + 1
        print(mylist[i] + mylist[k], end=" ")


def thirds():
    mylist = []
    num = eval(input("Enter the number of sentences:"))
    for x in range(num):
        sen = input("Enter Sentence" + str(x + 1) + ":")
        mylist.append(sen)
    for i in range(0, len(mylist)):
        c = mylist[i][0::3]
        print(c)


def word_average():
    sen = input("Enter a sentence:")
    j = len(sen.split())
    k = len(sen) - sen.count(" ")
    final = k/j
    print(final)


def pig_latin():
    sentence = input("Enter a sentence to convert to pig latin:")
    sentence = sentence.split()
    mids = " "
    answer = " "

    for i in sentence:
        letter = i[0]
        mid = mids+i[1::]
        answer = answer + (mid.lower() + letter.lower() + "ay")
        answer = answer.lstrip()
    print(answer)


if __name__ == '__main__':
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()
