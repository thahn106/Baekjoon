N = int(input())
dice = list(map(int,input().split()))
A, B, C, D, E, F = dice
if N == 1:
    print(sum(dice)-max(dice))
else:
    c3 = 4
    c2 = 4*(N-1)+4*(N-2)
    c1 = 4*(N-2)*(N-1)+(N-2)*(N-2)
    s3 = min(A,F)+min(B,E)+min(C,D)
    s2 = min(A+B,A+C,A+D,A+E,B+C,B+D,B+F,C+E,C+F,D+E,D+F,E+F)
    s1 = min(dice)
    print(c3*s3+c2*s2+c1*s1)
