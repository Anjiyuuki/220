# read file
# make everything lowercase
# take out all punctuation
# split on spaces -> list
# count each word -> word:count
# (Use dictionary, the key: word and value: frequency)
# sort result
# print top 5
def count_sort(tup):
    return tup[1]


def count(file_name):
    # read file
    text = open(file_name, 'r').read()
    # make everything lowercase
    text = text.lower()
    # take out all punctuation
    for ch in '[]`-~!@#$%^&*()_+={}|;:\'\\<>?,./\"”’“—':
        text = text.replace(ch, ' ')
    print(text)
    # split on spaces -> list
    words = text.split()
    print(len(words))
    # count each word -> word:count
    # (Use dictionary, the key: word and value: frequency)
    counts = {}
    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1
    print(counts)
    # ~~~~~~~~~~~~~~~~Another way to do the same above~~~~~~~~~~~~~~~~~~~
    # counts = {}
    # for word in words:
    #     counts[word] = counts.get(word, 0) + 1
    # print(counts)
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # now turns into tuple
    items = list(counts.items())
    print(items)
    # sort result
    items.sort(key=count_sort, reverse= True)
    print(items)
    # print top 5
    for i in range(5):
        word, count = items[i]
        print('{0:<15}{1:>5}'.format(word, count))
        # print(items[i])


if __name__=='__main__':
    count('alice.txt')
