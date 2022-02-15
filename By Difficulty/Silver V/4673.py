check  = [False]*10001
for i in range(10000):
    d = i+sum(list(map(int,list(str(i)))))
    if d<=10000:
        check[d] = True
for i in range(10001):
    if not check[i]:
        print(i)
