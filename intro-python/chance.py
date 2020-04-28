import random

def coin_flip():
    	return random.choice(['heads', 'tails'])


if coin_flip() == 'heads':
    	print('Heads - You win!')
else:
    	print('Tails - You lose!')
		

def die_roll():
	return random.randint(1,6)