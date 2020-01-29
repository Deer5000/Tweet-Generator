from random import randint, choice

my_file = open("/Users/khidrbrinkley/Desktop/dev/courses/cs1.2/in_class/words.txt")

lines = my_file.readlines()
#print(lines)

random_index = randint(0, len(lines)-1)

rand_item = lines[random_index]
#print(rand_item)

#my_file.close()

print(" ".join(word[0:-1] for word in lines))
