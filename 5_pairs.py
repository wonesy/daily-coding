def cons(a,b):
    def pair(f):
        return f(a,b)
    return pair

def car(pair):
    def _get_first(a,b):
        return a
    return pair(_get_first)

def cdr(pair):
    def _get_last(a,b):
        return b
    return pair(_get_last)

'''
example:
    car(cons(3,4)) ==> 3
    cdr(cons(3,4)) ==> 4
'''

print(car(cons(3,4)))
print(cdr(cons(3,4)))
