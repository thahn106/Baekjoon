H,M,S = map(int,input().split())
d,S =divmod(S+int(input()),60)
d,M =divmod(M+d,60)
H = (H+d)%24
print("{} {} {}".format(H,M,S))
