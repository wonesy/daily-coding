'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

from operator import mul    # or mul=lambda x,y:x*y
from fractions import Fraction
from functools import reduce

def nCk(n,k): 
  return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

def climbs(n):
    slots = n
    twos = 0
    count = 0 if n%2==1 else 1
    while slots > twos:
        count += nCk(slots, twos)
        slots -= 1
        twos += 1
    return count

print(climbs(4))
print(climbs(5))
print(climbs(6))
print(climbs(7))
print(climbs(8))
