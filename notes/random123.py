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

pig_latin()