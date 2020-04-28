import chance
from chance import coin_flip

name = input("What's your name?")
print("Hello,", name, "!")
print("Nice to meet you!")
input("do you want to play a game?")



flip = chance.coin_flip()

for n in range (11):
    if n % 2 == 0: 
        print(flip)
    else:
        print(n)