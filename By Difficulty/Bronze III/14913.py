a,d,k = map(int,input().split())
q,r = divmod(k-a, d)
if r or q<0:
    print('X')
else:
    print(q+1)
