from bisect import bisect_left

N = int(input())
a = list(map(int,input().split()))
a.sort()
M = int(input())
b =  list(map(int,input().split()))
for n in b:
    i = bisect_left(a,n)
    if i<N and  a[i] == n:
        print(1)
    else:
        print(0)
