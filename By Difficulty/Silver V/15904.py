ref = "UCPC"
cur = 0
possible = False
for c in input():
    if c == ref[cur]:
        cur +=1
    if cur == 4:
        possible = True
        break
if possible:
    print("I love UCPC")
else:
    print("I hate UCPC")
