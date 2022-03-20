for n in range(int(input())):
    a = list(map(int,input().split()))[1:]
    A = [0]*4
    for i in a:
        A[4-i]+=1
    b = list(map(int,input().split()))[1:]
    B = [0]*4
    for i in b:
        B[4-i]+=1
    A = tuple(A)
    B = tuple(B)
    if A>B:
        print("A")
    elif B>A:
        print("B")
    else:
        print("D")
