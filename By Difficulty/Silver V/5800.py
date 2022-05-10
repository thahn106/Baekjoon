for t in range(int(input())):
    r = sorted(list(map(int, input().split()))[1:])
    ma = max(r)
    mi = min(r)
    rm = 0
    for i in range(1,len(r)):
        rm = max(rm, r[i]-r[i-1])
    print(f"Class {t+1}")
    print(f"Max {ma}, Min {mi}, Largest gap {rm}")
