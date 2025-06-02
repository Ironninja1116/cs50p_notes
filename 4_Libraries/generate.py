#Section 4 Notes Segment 1

#using import keyword
'''
import random

coin = random.choice(["Heads","Tails"])
print(coin)
'''

#using from keyword
'''
from random import choice

coin = choice(["Heads","Tails"])
print(coin)
'''

#random randint
'''
import random

number = random.randint(1,10)
print(number)
'''

#random shuffle
'''
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
'''