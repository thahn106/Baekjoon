t = 1
n = int(input())
while n:
    names = []
    for i in range(n):
        names.append(input())
    count = [0]*n
    for i in range(2*n-1):
        ind, s = input().split()
        count[int(ind)-1]+=1
    ans = count.index(1)
    print("{} {}".format(t, names[ans]))
    n = int(input())
    t += 1
