S = input()
cur = S[0]
ans = 0
for c in S:
    if c!=cur:
        ans +=1
        cur = c
print((ans+1)//2)
