import sys
for t in range(int(input())):
    A,B = input().split()
    dis = []
    for a,b in zip(A,B):
        dis.append((ord(b)-ord(a))%26)
    sys.stdout.write("Distances: ")
    print(*dis)
