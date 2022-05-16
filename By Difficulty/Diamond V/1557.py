import sys
import time

sys.setrecursionlimit(30000)
MAX_PRIME = 100000
MAX_RES = 2000000000


def findprimes(a):
    prime = [True for i in range(MAX_PRIME + 1)]
    p = 2
    while(p * p <= MAX_PRIME):
        if prime[p]:
            for i in range(p * 2, MAX_PRIME + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, MAX_PRIME + 1):
        if (prime[p]):
            a.append(p)
    return a


start = time.time()
a = findprimes([])
print(f"time elapsed {time.time()-start}")

n = int(input())
start = time.time()
print(*a)


def countSquares(i, cur, k):
    print(f"{i=} {cur=} {k=}")
    print(*a[:10])
    square = a[i]*a[i]
    newCur = square*cur
    print(f"{newCur=}")
    if (newCur > k):
        return 0
    cnt = k // (newCur)
    tmp = countSquares(i + 1, cur, k)
    cnt += tmp
    tmp = countSquares(i + 1, newCur, k)
    cnt -= tmp
    print(f"{cnt=}")
    return cnt


print(f"{len(a)=}")

low = 1
high = MAX_RES
print(f"{low=}")
print(f"{high=}")

while low < high:
    mid = low + (high - low)//2
    print(f"{low=}")
    print(f"{high=}")
    print(f"{mid=}")
    c = countSquares(0, 1, mid)
    print(f"{c=}")
    c = mid - c
    if (c < n):
        low = mid + 1
    else:
        high = mid

print(low)
print(f"time elapsed {time.time()-start}")
