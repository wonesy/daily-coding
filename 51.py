'''

Suppose an arithmetic expression is given as a binary tree. Each leaf is an integer and each internal node is one of

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  +
        / \
       1   8
'''

from __future__ import annotations

class Node:
    def __init__(self, val: str, left: Node=None, right: Node=None):
        self.val = val
        self.left = left
        self.right = right

n3 = Node(str(3))
n2 = Node(str(2))
n4 = Node(str(4))
n5 = Node(str(5))
n8 = Node(str(111))
n1 = Node(str(1))
nplus1 = Node('+', left=n3, right=n2)
nplusm = Node('-', left=n1, right=n8)
nplus2 = Node('+', left=n4, right=nplusm)
nstar = Node('*', left=nplus1, right=nplus2)

def calc(b,a,operator):
    _a = int(a)
    _b = int(b)
    if operator == '+':
        return _a+_b
    if operator == '-':
        return _a-_b
    if operator == '*':
        return _a*_b
    if operator == '/':
        return _a/_b

def eval_tree(tree):
    def build_stack(tree,s=[]):
        if not tree.left and not tree.right:
            s.append(tree.val)
            return s

        if tree.left:
            s = build_stack(tree.left, s)
        if tree.right:
            s = build_stack(tree.right, s)

        s.append(tree.val)

        return s

    s = build_stack(tree)
    q = []
    for c in s:
        if c.isdigit():
            q.append(c)
        else:
            x = calc(q.pop(), q.pop(), c)
            q.append(x)
        
    return q.pop()

total = eval_tree(nstar)
print(total)


