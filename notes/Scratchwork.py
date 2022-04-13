# def Cypher(word, key):
#     encryptedString = ""
#     for char in word:
#         if char.isalpha() and char.isupper():
#             newVal = chr((ord(char) - ord('A') + key) % 26 + ord('A'))
#             encryptedString += newVal
#         elif char.isalpha() and char.islower():
#             newVal = chr((ord(char) - ord('a') + key) % 26 + ord('a'))
#             encryptedString += newVal
#         else:
#             encryptedString += char
#     return encryptedString
#
# def DeCypher(word, key):
#     encryptedString = ""
#     for char in word:
#         if char.isalpha() and char.isupper():
#             newVal = chr((ord(char) - ord('A') - key) % 26 + ord('A'))
#             encryptedString += newVal
#         elif char.isalpha() and char.islower():
#             newVal = chr((ord(char) - ord('a') - key) % 26 + ord('a'))
#             encryptedString += newVal
#         else:
#             encryptedString += char
#     return encryptedString
#
# key = 293222
# cVal = Cypher('Hello sussy Wen :moon:', key)
# print(cVal)
# Val = DeCypher(cVal, key)
# print(Val)

# def pig_latin():
#     sentence = input("Enter a sentence to convert to pig latin:")
#     sentence = sentence.split()
#     mids = " "
#     answer = " "
#
#     for i in sentence:
#         letter = i[0]
#         mid = mids+i[1::]
#         answer = answer + (mid.lower() + letter.lower() + "ay")
#         answer = answer.lstrip()
#     print(answer)
#
# pig_latin()

#
# for j in range(0, len(student_grades), 2):
#
#     weights += eval(student_grades[j])
#     grades = eval(student_grades[j + 1])
#     averages = (weights * grades)
#     averages = averages + j
#     averages = averages / 100
#     if weights < 100:
#         averages = " Weight is less than 100!"
#
#     if weights > 100:
#         averages = " Weight is more than 100!"
#
# output_file.write(str(student_info[0]) + str("'s average:") + str(
#     averages) + "\n")

# def letter_grade():
#     score = 'F' * 60 + 'D' * 10 + 'C' * 10 + 'B' * 10 + 'A' * 11
#     grade = eval(input("What is the student grade?"))
#     print("The student grade is " + score[grade] + ".")
#
# #letter_grade()
#
#
# def name_numeric():
#     alphabet = 'abcdefghijklmnopqrstuvwxyz'
#     name = input('enter the name:')
#     name_acc = 0
#     for character in name:
#         name_acc = name_acc + alphabet.find(character.lower()) + 1
#     print("The total score of the "+ name +" is {}".format(name_acc))
#
# #name_numeric()
#
# def in_sent():
#     sentence = input('Enter a sentense:')
#     print('There are {} words in your sent.'.format(len(sentence.split())))
#
# in_sent()

def fibonacci(num):
    n1, n2 = 1, 1
    fib_seq = []
    count = 0
    while count < num and num > 1:
        fib_seq.append(n1)
        result = n1 + n2
        n1 = n2
        n2 = result
        count += 1
    return fib_seq[num - 1]


def double_investment(principal, rate):
    year = 0
    total = total0 = principal
    while total < 2*total0:
        total = total + total * rate + 1
        year += 1
    return year


def syracuse(num):
    nums = [num]
    while num != 1:
        if (num % 2) == 0:
            res = num // 2
            nums.append(res)
            num = res
        else:
            res = num * 3 + 1
            nums.append(res)
            num = res
    return nums


def goldbach(num):
    # get primes
    primes = []
    val = 1
    while val <= num:
        count = 0
        i = 2
        while i <= val // 2:
            if val % i == 0:
                count = count + 1
                break
            i = i + 1
        if count == 0 and val != 1:
            primes.append(val)
        val = val + 1
    # goldy function
    if (
        num % 2 != 0
    ):
        return None

    idx_a = 0
    idx_b = 0

    prime_a = primes[idx_a]
    prime_b = primes[idx_b]

    while prime_a + prime_b != num:
        if prime_b == primes[-1]:
            idx_a = idx_a + 1
            idx_b = idx_a + 1
            prime_a = primes[idx_a]
            prime_b = primes[idx_b]
        else:
            idx_b = idx_b + 1
            prime_b = primes[idx_b]
    return [prime_a, prime_b]