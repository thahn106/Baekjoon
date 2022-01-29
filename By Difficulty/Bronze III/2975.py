s = input()
while s != "0 W 0":
    ac,t,am = s.split()
    ans = int(ac)
    if t == 'D':
        ans += int(am)
    else:
        ans -= int(am)
    if ans < -200:
        print("Not allowed")
    else:
        print(ans)
    s = input()
