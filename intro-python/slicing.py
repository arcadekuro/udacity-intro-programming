import time

def word_triangle(word):
    length = len(word)
    for n in range(length):
        print(word[:length - n])

#word_triangle("pizza")

n = 10
while n > 0:
    print(n)
    time.sleep(1)
    n -= 1
print('Blastoff!')