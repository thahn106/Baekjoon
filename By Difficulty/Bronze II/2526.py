N,P = map(int,input().split())

s = {}
s[N]=0
d = N
cur = 0
while True:
    d = (d*N)%P
    cur +=1
    if d in s:
        print(cur-s[d])
        break
    else:
        s[d]=cur
