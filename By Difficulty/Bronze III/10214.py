for t in range(int(input())):
    A,B = 0,0
    for i in range(9):
        a,b = map(int,input().split())
        A+=a
        B+=b
    if A>B:
        print("Yonsei")
    elif B>A:
        print("Korea")
    else:
        print("Draw")
