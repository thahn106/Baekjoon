s = input()
counts = [0]*26
for c in s:
    counts[ord(c)-65]+=1

if sum([i%2 for i in counts])>1:
    print("I'm Sorry Hansoo")
else:
    ans = ""
    mid = ""
    for i,n in enumerate(counts):
        c = chr(i+65)
        if n%2:
            mid = c
        ans += c*(n//2)
    print(ans+mid+ans[::-1])
