from random import random, randint
import sys

my_file = open("/Users/khidrbrinkley/Desktop/dev/courses/cs1.2/repos/gitclass/tweet_gen/words.txt")
lines = my_file.readlines()

for random_index in lines:
    random_index = randint(0, len(lines)-1)
    rand_item = lines[random_index]
    print(rand_item)

my_file.close()