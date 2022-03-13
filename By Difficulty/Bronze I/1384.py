import sys
t = 0
N = int(input())
while N:
    names = []
    nasties = []
    for i in range(N):
        A = input().split()
        names.append(A[0])
        for j in range(1,N):
            if A[j]=='N':
                f = (i-j)%N
                nasties.append((f,i))

    if t:
        sys.stdout.write("\n")
    sys.stdout.write(f"Group {t+1}\n")
    if len(nasties):
        for f,to in nasties:
            sys.stdout.write(f"{names[f]} was nasty about {names[to]}\n")
    else:
        sys.stdout.write("Nobody was nasty\n")

    t += 1
    N = int(input())

sys.stdout.flush()
