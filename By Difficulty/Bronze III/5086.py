A,B = map(int,input().split())
while A or B:
    if B%A ==0:
        print("factor")
    elif A%B==0:
        print("multiple")
    else:
        print("neither")
    A,B = map(int,input().split())
