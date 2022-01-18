
def c2n(char):
    if char==".":
        return None
    else:
        return (ord(char)-65)

class Node:
    def __init__(self, left=None,right=None):
        self.left=left
        self.right=right

N = int(input())
tree = [Node() for i in range(N)]
for i in range(N):
    name,l,r = input().split()
    tree[c2n(name)]=Node(left=c2n(l), right=c2n(r))

def preorder(n):
    ans = ""
    if n == None:
        return ans
    ans += chr(n+65)
    ans +=preorder(tree[n].left)
    ans +=preorder(tree[n].right)
    return ans

def inorder(n):
    ans = ""
    if n == None:
        return ans
    ans +=inorder(tree[n].left)
    ans += chr(n+65)
    ans +=inorder(tree[n].right)
    return ans

def postorder(n):
    ans = ""
    if n == None:
        return ans
    ans +=postorder(tree[n].left)
    ans +=postorder(tree[n].right)
    ans += chr(n+65)
    return ans

print(preorder(0))
print(inorder(0))
print(postorder(0))
