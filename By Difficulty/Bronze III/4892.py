n0 = int(input())
t = 1
while n0:
    n1 = 3*n0
    n2 = (n1+1)//2
    n3 = 3*n2
    n4 = n3//9
    if n1%2:
        p = "odd"
    else:
        p = "even"
    print("{}. {} {}".format(t,p,n4))
    t +=1
    n0 = int(input())
