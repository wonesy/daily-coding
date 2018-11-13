class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node({self.val})'


def serialize(root, string=None):
    string = root.val + '{'

    if root.left is not None:
        string += serialize(root.left, string) 
    
    string += ','

    if root.right is not None:
        string += serialize(root.right, string) 

    string += '}'

    return string 
    

def deserialize(s):
    nodes = []
    start = 0
    for i,char in enumerate(s):
        if char in ['{','}',',','\n']:
            val = s[start:i]
            start = i+1
            if val:       
                nodes.append(Node(val))
            elif char in [',','}'] and s[i-1] in [',','{']:
                nodes.append(None)

        if char == '}':
            right = nodes.pop()
            left = nodes.pop()
            root = nodes.pop()
            root.left = left
            root.right = right
            nodes.append(root)

    return nodes.pop()

node = Node('root', Node('left', Node('left.left'), Node('left.right')), Node('right'))

assert deserialize(serialize(node)).left.left.val == 'left.left'


