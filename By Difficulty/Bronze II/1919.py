s = input()
t = input()
S = [0 for i in range(26)]
T = [0 for i in range(26)]
for c in s:
    S[ord(c)-97]+=1
for c in t:
    T[ord(c)-97]+=1

ans = 0
for i in range(26):
    ans += abs(S[i]-T[i])
print(ans)
