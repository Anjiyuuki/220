"""
Name: Angie Bui
hw7.py

Problem: This assignment deals with the concept of files. Being able to read
write, edit and return information to specific files or send to information
to another file.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from encryption import encode, encode_better


def number_words(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    i = 0
    for line in in_file:
        for word in line.split():
            i = i + 1
            print((str(i)+" "+word), file=out_file)

    in_file.close()
    out_file.close()

    print(out_file)


def hourly_wages(in_file_name, out_file_name):
    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')
    for line in in_file:
        word = line.split(" ")
        wage = float(word[2])
        bonus = 1.65
        add_wage = wage + bonus
        hour = float(word[3])
        total = hour * add_wage
        print(("{}{}{}{}{:.2f}".format(word[0]," ",word[1]," ",total)),file=out_file)

    in_file.close()
    out_file.close()
    print(out_file)


def calc_check_sum(isbn):
    user_isbn = isbn.replace('-', '')
    answer = 0
    for i in range(10):
        value = user_isbn[::-1]
        index = eval(value[i])
        answer = answer + (index * (i + 1))
    return answer


def send_message(file_name, friend_name):
    in_file = open(file_name, 'r')
    read_file = in_file.readlines()
    out_file = open(friend_name + '.txt', 'w')

    for line in read_file:
        first_var = line.split()
        for word in first_var:
            word += word
        print(line.replace('\n', ''), file=out_file)

    in_file.close()
    out_file.close()
    print(friend_name)


def send_safe_message(file_name, friend_name, key):
    in_file = open(file_name, 'r')
    friend_txt = friend_name + ".txt"
    out_file = open(friend_txt, 'w')
    encrypted_sent = ""
    for line in in_file.readlines():
        encrypted_line = encode(line.rstrip(), key)
        encrypted_sent = encrypted_sent + encrypted_line + "\n"
    print(encrypted_sent.rstrip(), file=out_file)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    in_file_name = open(file_name, 'r')
    in_pad_file = open(pad_file_name, 'r')
    friend_file = friend_name + '.txt'
    better_friend = open(friend_file, 'w')
    read_message = in_file_name.read()
    read_key = in_pad_file.read()
    uncrack_message = encode_better(read_message, read_key)
    print(uncrack_message, file=better_friend)


if __name__ == '__main__':
    pass
