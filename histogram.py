import random
from random import randint
import sys
# import dictionary_words

any_file = "words.txt"
any_lines = open(any_file, "r")

histograms = {"one": 2,
            "fish": 4, "red": 2, "blue": 2
        }

def histo():
    file = open("words.txt", "r")
    lines = file.readlines()

    histo = {}

    for line in lines:
        words = line.rstrip('\n').split(" ")
        for word in words:
            if word in histo.keys():
                histo[word] += 1
            else:
                histo[word] = 1

    return histo

def unique_words():
    count = 0
    for word in histograms:
        #check if word is unique, only seen once
        if histograms[word] == 1:
            count += 1
        else:
            return('Err')
    return(count)



def sample(histo):
    tokens = 0
    for k,v in histo.items():
        tokens += v
    dart = randint(1, tokens)
    fence = 0
    for word,count in histo.items():
        fence += count
        if fence >= dart:
            return word



def frequency():
    for word in histograms:
        print(f'{word} was repeated {histograms[word]} times.')



if __name__ == '__main__':
    print(histo())
    print(unique_words())
    print(frequency())