# random

"""
An everyday computing problem is making a random choice. Computers are not good at being random. The random library generates
pseudo-random numbers that are suitable for most purposes. You can use these for games or simple statistical checks.

The random library is part of the Python standard library. You can use it by importing it into your code. The random library
contains a number of functions that you can use to generate random numbers.


In the runnable example, you can see how you would generate a random float, integer or choice. You can also shuffle existing data structures.

"""

# Runnable example:

import random

print(f'A random float between 0 & 1.0: {random.random()}')
print(f'A random int between 0 & 10: {random.randrange(11)}')
print('A random choice from a list: ' + random.choice(['paper', 'scissors', 'rock']))
deck = ['hearts', 'diamonds', 'spades', 'clubs']
random.shuffle(deck)
print(deck)

