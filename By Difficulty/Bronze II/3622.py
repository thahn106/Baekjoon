A, a, B, b, P = map(int,input().split())
if (A<=P and B<=P) and  (A<=b or B<=a or A+B<=P):
    print("Yes")
else:
    print("No")
