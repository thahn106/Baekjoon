A,B,C = map(int,input().split())
cocktails = [A,B,C,A*B,B*C,A*C,A*B*C]
evens = []
odds = []
for c in cocktails:
    if c%2:
        odds.append(c)
    else:
        evens.append(c)
if odds:
    print(max(odds))
else:
    print(max(evens))
