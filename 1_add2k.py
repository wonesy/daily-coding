#!/usr/bin/env python3

'''
given a list of numbers and a number k, return whether any two numbers from the lsit add up to k
'''


a = [10,15,3,7]
b = [10,15,3,75]
c = [4,15,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,7,7,78,8,9,9,11,7]
d = [10,15,3,71,2342353245,11,12,13,14,15,16,17,18]
e = [10,15,3,7,5]

def find_values(k, values):
    past = {}
    for i in values:
        if i >= k:
            continue
        complement = (k-i)
        if past.get(complement, None):
            return True
        past[i] = 1
    return False

print(find_values(15, a))
print(find_values(15, b))
print(find_values(15, c))
print(find_values(15, d))
print(find_values(15, e))

