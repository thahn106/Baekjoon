for t in range(int(input())):
    A,B,C,D,E = map(int,input().split())
    ans = 350.34*A+230.90*B+190.55*C+125.30*D+180.90*E
    print("${:.2f}".format(ans))
