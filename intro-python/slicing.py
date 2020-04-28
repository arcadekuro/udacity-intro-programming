import time

def word_triangle(word):
    length = len(word)
    for n in range(length):
        print(word[:length - n])

#word_triangle("pizza")

