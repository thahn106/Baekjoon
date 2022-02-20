counts = [0]*26
S = input()
for c in S:
    counts[ord(c)-97]+=1
print(*counts)
