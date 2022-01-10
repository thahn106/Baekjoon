import sys
input = sys.stdin.buffer.readline
from math import log, ceil

N,M = map(int,input().split())

nums = [int(input()) for n in range(N)]

class Node:
    min = 2**63
    max = -2**63
    def __init__(self):
        pass

class SegTree:
    nodes = []
    mins, maxs = [], []
    h = 0
    def __init__(self,size):
        self.h = ceil(log(size)/log(2))
        self.treeSize = 2**(self.h+1)
        self.nodes = [Node() for i in range(self.treeSize)]
        self.build(1, size, 1)

    def build(self, start, end, index):
        if start == end:
            self.nodes[index].min = nums[start-1]
            self.nodes[index].max = nums[start-1]
            return index
        mid = (start+end)//2
        l = self.build(start,mid, index*2)
        r = self.build(mid+1,end, index*2+1)
        self.nodes[index].min = min(self.nodes[l].min, self.nodes[r].min)
        self.nodes[index].max = max(self.nodes[l].max, self.nodes[r].max)
        return index

    def find(self, start, end, a, b, ind):
        # print("start: {} end: {} ind: {}".format(start,end,ind))
        if b < start or a > end:
            return Node()
        if a <= start and end <=b:
            return self.nodes[ind]
        mid = (start+end)//2
        ln = self.find(start,mid,a,b,ind*2)
        rn = self.find(mid+1,end,a,b,ind*2+1)
        ans = Node()
        ans.min = min(ln.min, rn.min)
        ans.max = max(ln.max, rn.max)
        return ans

ST = SegTree(N)

for m in range(M):
    a,b= map(int,input().split())
    ans = ST.find(1,N,a,b,1)
    print("{} {}".format(ans.min, ans.max))
