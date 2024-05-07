# random Challenge

import random

def ten_rand_nums():
    return [random.randint(0, 100) for x in range(10)]

result = ten_rand_nums()

print(result)

random.shuffle(result)

print(result)
