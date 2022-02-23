def az(s):
    return "0"*(6-len(s))+s

for t in range(int(input())):
    time = list(map(int,input().split(':')))
    a = ["".join(az(bin(i)[2:])) for i in time]
    b = ["".join([a[j][i] for j in range(3)]) for i in range(6)]
    print("".join(b), "".join(a))
