# Python3.7

from __future__ import annotations

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0a
  /  \
 1b   0c
     / \
   1e   0f
  /  \   \
 1g  1h   0i

This indicates that all leaves are considered trees with identical subtree values

'''

class Node:
    def __init__(self, val:int, left:Node = None, right:Node = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f'Node({self.val})'

    def val_matches_children(self):
        if self.left and self.left.val == self.val:
            return True

        if self.right and self.right.val == self.val:
            return True

        return False

def find_univals(root:Node, pval:int=None) -> (int, bool):

    # If this is a leave, it's a unival tree
    if not root.left and not root.right:
        print(f'Leaf: value={root.val}')
        return 1, True

    lmatches = rmatches = True
    lcount = rcount = 0

    if root.left:
        lcount, lmatches = find_univals(root.left, root.val)

    if root.right:
        rcount, rmatches = find_univals(root.right, root.val)

    ret_match = lmatches and rmatches and root.val_matches_children() 
    ret_count = lcount + rcount

    if ret_match:
        ret_count += 1

    print(f'count={ret_count} - match={ret_match} - val={root.val} - pval={pval}')
    return ret_count, (ret_match and (root.val == pval))

i = Node(0)
h = Node(1)
g = Node(1)
f = Node(0)
e = Node(1,left=g, right=h)
c = Node(0,left=e,right=f)
b = Node(1)
a = Node(0,left=b,right=c)

x = find_univals(a)
print(x)
