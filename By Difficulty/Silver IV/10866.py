import sys
input = sys.stdin.readline

D = 20000
q = [0 for i in range(20000)]
head = 0
tail = 0
for n in range(int(input())):
    a = input().strip()
    if a[:2]=="pu":
        if a[5:7]=="fr":
            a,b = a.split()
            head -=1
            q[head]=b
        else:
            a,b = a.split()
            q[tail]=b
            tail +=1
    elif a[:2]=="po":
        if tail>head:
            if a[4:6]=="fr":
                print(q[head])
                head+=1
            else:
                print(q[tail-1])
                tail-=1
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
