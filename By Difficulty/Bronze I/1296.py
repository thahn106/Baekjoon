S = input()
N = int(input())

names = []
for n in range(N):
    names.append(input())
names.sort()

probs = []
for cur in names:
    cur += S
    L,O,V,E = 0,0,0,0
    for c in cur:
        if c=='L':
            L+=1
        elif c == 'O':
            O+=1
        elif c == 'V':
            V+=1
        elif c == 'E':
            E+=1
    A =[L,O,V,E]
    p = 1
    for i in range(3):
        for j in range(i+1,4):
            p*= A[i]+A[j]
    probs.append(p%100)

cur = -1
ans = ""
for n in range(N):
    if probs[n]>cur:
        cur = probs[n]
        ans = names[n]
print(ans)
