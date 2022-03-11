import sys
input = sys.stdin.buffer.readline
from math import log, ceil

N = int(input())
graph = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

#PREPROCESSING
start = 0  #ROOT NODE
vst, order, q = [False for i in range(N)], [], [start]
heights = [0 for i in range(N)]
while q:
    cur_node = q.pop()
    order.append(cur_node)
    vst[cur_node] = True
    for nbr in graph[cur_node]:
        if not vst[nbr]:
            q.append(nbr)
            heights[nbr]=heights[cur_node]+1

first = [0 for i in range(N)]
for i in range(N):
    first[order[i]]=i

class Node:
    min = 2**63
    ind = -1
    def __init__(self):
        pass

class SegTree:
    nodes = []
    min = N
    h = 0
    def __init__(self,size):
        self.h = ceil(log(size)/log(2))
        self.treeSize = 2**(self.h+1)
        self.nodes = [Node() for i in range(self.treeSize)]
        self.build(1, size, 1)

    def build(self, start, end, index):
        if start == end:
            self.nodes[index].min = heights[start-1]
            self.nodes[index].ind = start-1
            print("ind:{} min:{}".format(start-1, heights[start-1]))
            return index
        mid = (start+end)//2
        l = self.build(start,mid, index*2)
        r = self.build(mid+1,end, index*2+1)
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
        if ln.min<rn.min:
            ans.ind = ln.ind
        else:
            ans.ind = rn.ind
        return ans

ST = SegTree(N)

M = int(input())
for m in range(M):
    a,b= map(int,input().split())
    ans = ST.find(1,N,a,b,1)
    print("{}".format(ans.ind))







M = int(input())
