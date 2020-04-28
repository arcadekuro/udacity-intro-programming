#def say_hello():
#    return "Hello!"
#
#say_hello()
import chance
from chance import coin_flip

"""
def confuse():
    print("bears")
    return 42

confuse()
"""""
def more_confused():
    2 + 2

# print(more_confused())

flip = chance.coin_flip()

def chance_game(n):
    if flip == 'heads':
        print(n + 10)
    else:
        if flip == 'tails':
            print(n + 20)

chance_game(20)