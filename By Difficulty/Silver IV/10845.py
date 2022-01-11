import sys
input = sys.stdin.readline

q = [0 for i in range(10010)]
head = 0
tail = 0
for n in range(int(input())):
    a = input().strip()
    if a[:2]=="pu":
        a,b = a.split()
        q[tail]=b
        tail +=1
    elif a[:2]=="po":
        if tail>head:
            print(q[head])
            head+=1
        else:
            print(-1)
    elif a[:2]=="si":
        print(tail-head)
    elif a[:2]=="em":
        if tail>head:
            print(0)
        else:
            print(1)
    elif a[:2]=="fr":
        if tail>head:
            print(q[head])
        else:
            print(-1)
    elif a[:2]=="ba":
        if tail>head:
            print(q[tail-1])
        else:
            print(-1)
    else:
        pass
