N = int(input())
a = [int(input()) for i in range(N)]

for d in range(2):
    c = 0
    cur = 0
    for i in range(N):
        if a[i]>cur:
            c+=1
            cur = a[i]
    print(c)
    a.reverse()
