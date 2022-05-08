N = int(input())
a = '@'*N
s = ' '*N
for i in range(N):
    print(a*3+s+a)
for i in range(3*N):
    print(a+s+a+s+a)
for i in range(N):
    print(a+s+a*3)
