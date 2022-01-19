for t in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    dpa = a.copy()
    dpb = b.copy()
    if n>1:
        dpa[1] = a[1]+dpb[0]
        dpb[1] = b[1]+dpa[0]
        for i in range(2,n):
            dpa[i] = a[i]+max(dpb[i-1],dpb[i-2])
            dpb[i] = b[i]+max(dpa[i-1],dpa[i-2])

    print(max(dpa[-1],dpb[-1]))
