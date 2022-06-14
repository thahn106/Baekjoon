for t in range(int(input())):
    a = int(input())
    a = sum(list(map(int, input().split())))
    if a < 0:
        print("Left")
    elif a > 0:
        print("Right")
    else:
        print("Equilibrium")
