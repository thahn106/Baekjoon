a,c,e = map(int,input().split())
x,y,z = map(int,input().split())
if z<e:
    print('E')
elif 2*y<c:
    print('E')
elif y<c:
    print('D')
elif 2*x<a:
    print('C')
elif x<a:
    print('B')
else:
    print('A')
