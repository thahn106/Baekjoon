import sys
input = sys.stdin.buffer.readline
T = int(input())
for t in range(T):
    s = input()
    N = int(input().strip())
    sum = 0
    for i in range(N):
        sum +=int(input())
    if sum%N:
        print("NO")
    else:
        print("YES")
