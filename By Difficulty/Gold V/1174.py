from math import comb

N = int(input())
ans = []
d = 1
if N>1023:
    print(-1)
else:
    while comb(10,d)<N:
        N -= comb(10,d)
        d += 1
    for i in range(d):
        j = d-1-i
        if j:
            while comb(j, d-i-1)<N:
                N -= comb(j, d-i-1)
                j+=1
        else:
            j = N-1
        ans.append(str(j))
    print("".join(ans))
