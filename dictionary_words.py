import sys
from random import random, randint

file = open("words.txt", "r")

lines = file.readlines()

def dict_words():
    words_dictionary = {}

    for line in lines:
        words = line.rstrip('\n').split()
        for word in words:
            if word in words_dictionary.keys():
                words_dictionary[word] += 1
            else:
                words_dictionary[word] = 1


    return words_dictionary




if __name__ == '__main__':
    print(dict_words())