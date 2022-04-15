def user_name():
    first_name = input("Enter first name:")
    last_name = input("Enter last name:")
    first_letter = first_name[0]
    last_seven = last_name[:7]
    user = first_letter + last_seven
    print("Username:" + user)
#user_name()


def get_month():
    months = "JanFebMarAprMayJunJul"
    month_number = eval(input("Enter month number:"))
    # we want to get feb, so we have to go from 3 to 6
    start_index = 3 * month_number - 3
    end_index = start_index + 3
    month = months[start_index:end_index]
    print("That is:", month)
#get_month()


def get_month_again():
    months = ["Jan", "Feb", "Mar","apr", "may", "Jun","Jul"]
    month_number = eval(input("Enter month number:"))
    # we want to get feb, so we have to go from 3 to 6
    index = month_number - 1
    month = months[index]
    print("That is:", month)
#get_month_again()


def encode():
    word = input("Enter a word:")
    #for i in range(0, len(word)):
        #letter = word[0]
    for letter in word:
        num = ord(letter)
        print(num, end=" ")
#encode()


def encode_or():
    ordinals = []
    word = input("Enter a word:")
    for letter in word:
        num = ord(letter)
        ordinals.append(num)
    print(ordinals)
#encode_or()


def decode():
    numbers = input("Enter encoded message:")
    number_list = numbers.split(" ")
    for numb in number_list:
        letter = chr(eval(numb))
        print(letter, end="")
#decode()


def decode_s():
    numbers = input("Enter encoded message:")
    number_list = numbers.split(" ")
    my_string = ""
    for numb in number_list:
        letter = chr(eval(numb))
        my_string = my_string + letter
    print(my_string)
#decode_s()


def print_poem():
    my_poem = open('poem.txt', 'r')
    poem_txt = my_poem.read()
    print(poem_txt)
    my_poem.close()
#print_poem()


def print_file_lines():
    my_poem = open('poem.txt', 'r')
    for i in range(5):
        line = my_poem.readline()
        print(line, end=' ')
        # or you can type print(line[:-1])

#print_file_lines()

def print_file_list():
    my_poem = open('poem.txt', 'r')
    # or you can do for line in my_poem() same results will happen
    for line in my_poem.readlines():
        print(line[:-1]) #takes out the default new lines character



# This creates a new file
output_file = open('output.txt', 'w')
print("Hello World!", file = output_file)

