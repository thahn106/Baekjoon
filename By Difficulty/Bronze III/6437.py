from math import ceil
t = 0
p,s = map(int,input().split())
while p and s:
    if s == 1:
        ans = "Hole-in-one."
    elif s == p-3:
        ans = "Double eagle."
    elif s == p-2:
        ans = "Eagle."
    elif s == p-1:
        ans = "Birdie."
    elif s == p:
        ans = "Par."
    elif s == p+1:
        ans = "Bogey."
    else:
        ans = "Double Bogey."
    if t:
        print("")
    print(f"Hole #{t+1}")
    print(ans)
    t += 1
    p,s = map(int,input().split())
