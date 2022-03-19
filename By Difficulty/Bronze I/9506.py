from math import sqrt, floor

n = int(input())
while n != -1:
    fac = []
    rfac =  []
    for i in range(1, floor(sqrt(n))+1):
        d,r = divmod(n,i)
        if r == 0:
            fac.append(i)
            if d!=n and d!=i:
                rfac.append(d)
    fac += rfac[::-1]
    if sum(fac) == n:
        print(f"{n} = "+" + ".join(list(map(str,fac))))
    else:
        print(f"{n} is NOT perfect.")

    n = int(input())
