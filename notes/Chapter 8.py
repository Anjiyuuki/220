def first_while():
    for i in range(5):
        print(i, end='')
    print('\n{0:*<70}'.format(''))
    i = 0
    while i <5:
        print(i, end='')
        i = i + 1


# def is_equal(p1, p2):
#     if p1.getX() == p2.getX() and p1.getY() = p2.getY():
#         return True
#     return False

def is_game_over(player_one_points, player_two_points):
    if player_one_points >= 15 or player_two_points >= 15:
        return True
    return False
#


def i_game_over(p_one_points, p_two_points):
    if p_one_points >= 15 and p_one_points - p_two_points >= 2:
        return True
    if p_two_points >= 15 and p_two_points - p_one_points >= 2:
        return True
    return False
    # basically the game is over if one of the person wins by two


# if __name__ == '__main__':
#     #first_while()
#     player_1 = 9
#     player_2 = 11
#     game_over = is_game_over(player_1, player_2)
#     while not is_game_over(player_1, player_2):
#         x = eval(input("Enter a number"))
#         player_1 = player_1 + x
#         print(player_1, player_2)
#     print("game_over")

def deMorgan_one(input_value):
    a = input_value[0]
    b = input_value[1]
    return not(a or b) == (not a and not b)


def deMorgan_test():
    my_tests = [
        [True, True], [True, False], [False, True], [False, False]
    ]

    for test in my_tests:
        # a = test[0]
        # b = test[1]
        # result = deMorgan_one(a, b)
        # print(result)
        result = deMorgan_one(test)
        print(result)
        print('input:{}, result:{}'.format(test,result))


def whoops():
    user_input = input("Do you want to transfer all your money?")
    if user_input == 'y' or 'yes':
        print("Tranfering...")
    else:
        print('good idea.')


def ice_cream():
    answer = input('What is your fav icecream [Vanilla]:')
    favorite = answer or 'Vanilla'
    print(favorite)
    # if answer:
    #     favorite = answer
    #     print(favorite)
    # else:
    #     favorite = 'Vanilla'
    #     print(favorite)


def average():
    n = eval(input("How many numbers do you have:"))
    sum = 0
    for i in range(n):
        user_input = eval(input("Enter a number:"))
        sum = sum + user_input
    print('The average is {}'.format(sum/n))


def while_average():
    n = eval(input("How many numbers do you have:"))
    sum = 0
    count = 0
    while count < n:
        user_input = eval(input("Enter a number:"))
        sum = sum + user_input
        count = count + 1
    print('The average is {}'.format(sum / n))


def while_interactive():
    ans = 'y'
    sum = 0
    count = 0
    # getting the first letter from the string, so if it has the letter Y, it will run again
    while ans[0] == 'y':
        user_input = eval(input("Enter a number:"))
        sum = sum + user_input
        count = count + 1
        ans = input('Do you have any more numbers:')

    print('The average is {}'.format(sum / count))


def while_sentinel():
    user_input = 1
    sum = 0
    count = 0
    while user_input >= 0:
        user_input = eval(input("Enter a number:"))
        sum = sum + user_input
        count = count + 1

    print('The average is {}'.format(sum / count))


def average_sentinels_enter():
    acc = 0
    count = -1
    num = input("Enter a number(enter to exit)")
    while num != '':
        acc = acc + eval(num)
        count = count + 1
        num = input("Enter a number(enter again to exit)")
    print("average: {}".format(acc/count))


def average_sentinels():
    acc = 0
    count = -1
    num = 0
    while num >= 0:
        acc = acc + num
        count = count + 1
        num = eval(input("Enter a number(negative ti exit)"))
    print("average:{}".format(acc/count))


def average_file():
    acc = 0
    count = 0
    file_name = 'file.data.txt'
    file = open(file_name, 'r')
    for line in file:
        num = eval(line)
        acc = acc + num
        count = count + 1
    print("average:{}".format(acc / count))


def average_file_while():
    acc = 0
    count = 0
    file_name = 'file.data.txt'
    file = open(file_name, 'r')
    line = file.readline()
    while line != '':
        num = eval(line)
        acc = acc + num
        count = count + 1
        line = file.readline()
    print("average:{}".format(acc / count))


def average_file_while_nested():
    acc = 0
    count = 0
    file_name = 'nested.data.txt'
    file = open(file_name, 'r')
    line = file.readline()
    while line != '':
        # right now it is a string in the nested.data.txt
        # need to break it up into elements
        nums_string = line.split(',')
        i = 0
        while i < len(nums_string):
            num = nums_string[i]
            acc = acc + eval(num)
            count = count + 1
            i = i + 1
        line = file.readline()
    print("Average:{}".format(acc / count))


if __name__ == '__main__':
    #deMorgan_test()
    #whoops()
    #ice_cream()
    #average()
    #while_average()
    #while_interactive()
    #average_sentinels_enter()
    #average_file()
    #average_file_while()
    average_file_while_nested()









