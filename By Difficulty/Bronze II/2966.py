N = int(input())
S = input()
A,B,G = 0,0,0
for i,c in enumerate(S):
    if c == "ABC"[i%3]:
        A+=1
    if c == "BABC"[i%4]:
        B+=1
    if c == "CCAABB"[i%6]:
        G+=1
m = max(A,B,G)
print(m)
if A == m:
    print("Adrian")
if B == m:
    print("Bruno")
if G == m:
    print("Goran")
