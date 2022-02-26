n,p,h = map(int,input().split())

for i in range(n):
    k = int(input())
    if k<p:
        print(f"NTV: Dollar dropped by {p-k} Oshloobs")
    elif k>h:
        print(f"BBTV: Dollar reached {k} Oshloobs, A record!")
        h = k
    p = k
