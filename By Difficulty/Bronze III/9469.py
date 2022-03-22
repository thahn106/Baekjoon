for p in range(int(input())):
    N,D,A,B,F = map(float,input().split())
    N = p+1
    print(N,F*D/(A+B))
