N = int(input())
cand  = [0 for i in range(26)]
for i in range(N):
    cand[ord(input()[0])-97]+=1
if max(cand)<5:
    print("PREDAJA")
else:
    ans = ""
    for i in range(26):
        if cand[i]>=5:
            ans += chr(i+97)
    print(ans)
