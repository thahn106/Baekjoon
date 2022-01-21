H,M = map(int,input().split())
d,M =divmod(M+int(input()),60)
H = (H+d)%24
print("{} {}".format(H,M))
