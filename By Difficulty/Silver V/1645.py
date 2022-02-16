N = int(input())
k = [int(input()) for i in range(N)]
k.sort()

for i in range(N):
    if k[i]<=i:
        print(i+1)
        break
