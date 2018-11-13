x = [3,4,-1,1]
y = [1,2,0]
z = [8,5,2,9,6,3,1,-100]


def find_missing_positive_integer(a):
    a.sort()

    for i,val in enumerate(a):
        if i == 0 or val <= 1:
            continue

        if a[i-1] + 1 != a[i]:
            lowest_pos = a[i-1]+1
            return lowest_pos if lowest_pos > 0 else 1

    res = a[-1] + 1

    if res > 0:
        return res
    return 1
        

print(find_missing_positive_integer(x))
print(find_missing_positive_integer(y))
print(find_missing_positive_integer(z))
