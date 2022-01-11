import sys
input = sys.stdin.readline

q = [0 for i in range(10000)]
size = 0
for n in range(int(input())):
    a = input().strip()
    if a[:2]=="pu":
        a,b = a.split()
        q[size]=b
        size +=1
    elif a[:2]=="po":
        if size:
            print(q[size-1])
            size-=1
        else:
            print(-1)
    elif a[:2]=="si":
        print(size)
    elif a[:2]=="em":
        if size:
            print(0)
        else:
            print(1)
    else:
        if size:
            print(q[size-1])
        else:
            print(-1)
