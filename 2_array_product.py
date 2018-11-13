#!/usr/bin/env python3

a = [1,2,3,4,5]
b = [0,1,2,3,4,5]
c = [1,0,0,2,3,4,5]

def product(a):
    zeros = 0
    max_product = 1
    result = []

    for x in a:
        if x == 0:
            zeros += 1
            if zeros > 1:
                break
        else:
            max_product *= x

    if zeros >= 2:
        return ([0] * len(a))

    for x in a:
        if zeros == 1 and x != 0:
            result.append(0)
        elif zeros == 1 and x == 0:
            result.append(max_product)
        else:
            result.append(int(max_product/x))
    return result

print(product(a))
print(product(b))
print(product(c))
