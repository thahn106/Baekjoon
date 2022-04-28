import sys
B = [0]*2000005
for i in range(int(input())):
    t = int(sys.stdin.readline().strip())
    B[1000002-t] = 1
for i, c in enumerate(B):
    if c:
        sys.stdout.write(str(1000002-i)+'\n')
sys.stdout.flush()
