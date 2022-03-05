def encode(msg, key):
    length = len(msg)
    final_message = ""
    for i in range(length):
        letter = msg[i]
        coded_msg = ord(letter) + key
        new_msg = chr(coded_msg)
        final_message = final_message + new_msg
    return final_message

def encode_better(msg_bet, key_better):
    cipher_list = []
    answer = []
    for message in range(len(msg_bet) - len(key_better)):
        key_better = key_better + (key_better[message % len(key_better)])
    for letter in range(len(msg_bet)):
        shift = ((ord(msg_bet[letter])-65) + (ord(key_better[letter])-65)) % 58
        shift = shift + ord('A')
        cipher_list.append(shift)
    for number in range(len(cipher_list)):
        decode_better = chr(cipher_list[number])
        answer.append(decode_better)
    answer_better = ''.join(answer)
    return answer_better
   
