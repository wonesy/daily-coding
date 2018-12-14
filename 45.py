"""
Using a function rand5() that returns an integer from 1 to 5 

(inclusive) with uniform probability, implement a function rand7() that returns an integer from 1 to 7 (inclusive).
"""

import random
from functools import reduce

def rand5():
    return random.randint(1,5)

def rand7():
    """
    2 rolls, gives us 25 options

    roll1 x roll2 matrix

    - 1 2 3 4 5
    -+---------
    1|1 1 1 6 7
    2|2 2 2 6 7
    3|3 3 3 6 7
    4|4 4 4 x x
    5|5 5 5 x x
    """
    roll1 = rand5()
    roll2 = rand5()

    if roll2 < 3:
        return roll1

    if roll1 < 3:   # reroll, x in the matrix
        return rand7()

    if roll2 == 4:
        return 6

    if roll2 == 5:
        return 7


def full_test():
    results = [0,0,0,0,0,0,0]
    for _ in range(1000):
        x = rand7()
        results[x-1] += 1
    print(results)

if __name__ == '__main__':
    print(rand7())
    full_test()


