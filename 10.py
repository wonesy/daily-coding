'''
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

def _timer(f, n):
    msleep(n)
    f()

def scheduler(f, n):
    thread(_timer(f, n))
