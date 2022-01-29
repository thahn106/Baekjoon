A,B,C,D = map(int,input().split())
P = list(map(int,input().split()))

for p in P:
    p -= 1
    ans = int(p%(A+B)<A) + int(p%(C+D)<C)
    print(ans)
