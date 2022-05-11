N, T = map(int,input().split())
t = (T-1)%(4*N-2)
if t>2*N-1:
    print(4*N-1-t)
else:
    print(t+1)
