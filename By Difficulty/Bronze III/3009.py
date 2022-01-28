x= []
y= []
for i in range(3):
    a,b = map(int,input().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
print("{} {}".format(sum(x)-2*x[1],sum(y)-2*y[1]))
