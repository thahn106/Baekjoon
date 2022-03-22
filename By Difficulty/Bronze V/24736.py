S = [6,3,2,1,2]

X = list(map(int,input().split()))
x = 0
for a,b in zip(S,X):
    x += a*b

Y = list(map(int,input().split()))
y = 0
for a,b in zip(S,Y):
    y += a*b
print(x,y)
