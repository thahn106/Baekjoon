import sys
for t in range(int(input())):
    grid = [sys.stdin.readline().strip() for i in range(5)]
    A = False
    B = False

    for i in range(5):
        if A and B:
            break
        for j in range(3):
            if A and B:
                break
            rA,rB,cA,cB = True,True,True,True
            for k in range(3):
                if grid[i][j+k]=='A': rB = False
                else: rA = False
                if grid[j+k][i]=='A': cB = False
                else: cA = False
            if rA or cA: A = True
            if rB or cB: B = True
    for i in range(3):
        if A and B:
            break
        for j in range(3):
            if A and B:
                break
            rA,rB,cA,cB = True,True,True,True
            for k in range(3):
                if grid[i+k][j+k]=='A': rB = False
                else: rA = False
                if grid[i+2-k][j+k]=='A': cB = False
                else: cA = False
            if rA or cA: A = True
            if rB or cB: B = True
    if A and B:
        sys.stdout.write("draw\n")
    elif A:
        sys.stdout.write("A wins\n")
    elif B:
        sys.stdout.write("B wins\n")
    else:
        sys.stdout.write("draw\n")
sys.stdout.flush()
