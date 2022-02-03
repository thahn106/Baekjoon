from math import floor
A,B,C,D = map(int,input().split())
while A or B or C or D:
    A,B = max(A,B),min(A,B)
    C,D = max(C,D),min(C,D)
    ans = floor(100*min(1,min(C/A,D/B)))
    print("{}%".format(ans))
    A,B,C,D = map(int,input().split())
