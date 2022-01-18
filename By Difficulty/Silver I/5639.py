import sys
sys.setrecursionlimit(10020)
arr = []
try:
    while True:
        s = input()
        arr.append(int(s))
except EOFError as e:
    pass

class Node:
    def __init__(self,val = None, left=None,right=None):
        self.val = val
        self.left=left
        self.right=right

def construct(arr):
    if not arr:
        return None
    v = arr[0]
    i = 1
    while i < len(arr) and arr[i]<v:
        i+=1
    l = construct(arr[1:i])
    r = construct(arr[i:])
    return Node(val = v, left=l, right=r)

root = construct(arr)

def postorder(node):
    ans = []
    if node == None:
        return ans
    ans += postorder(node.left)
    ans += postorder(node.right)
    ans += [ node.val ]
    return ans

ans = postorder(root)
for n in ans:
    print(n)
