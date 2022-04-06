from math import pi
A,P1 = map(int,input().split())
R,P2 = map(int,input().split())

if (R*R*pi)/P2>A/P1:
    print("Whole pizza")
else:
    print("Slice of pizza")
