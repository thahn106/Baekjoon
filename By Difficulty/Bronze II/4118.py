N = int(input())
while N:
    line = [0]*49
    for n in range(N):
        for i in input().split():
            line[int(i)-1]=1
    if sum(line)==49:
        print("Yes")
    else:
        print("No")
    N = int(input())
