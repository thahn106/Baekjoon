def t(n):
    if n==0:
        return("00")
    elif n<10:
        return "0"+str(n)
    else:
        return str(n)


T,A,B = map(int,input().split())
while T or A or B:
    T *= 3600
    T = round(T*(B-A)/(A*B))
    H,T = divmod(T,3600)
    M,S = divmod(T,60)
    print("{}:{}:{}".format(str(H),t(M),t(S)))
    T,A,B = map(int,input().split())
