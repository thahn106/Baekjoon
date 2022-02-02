h1,m1,s1 = map(int,input().split(":"))
h2,m2,s2 = map(int,input().split(":"))

dif = ((h2-h1)*60*60+(m2-m1)*60+(s2-s1)) % (24*60*60)

H,d = divmod(dif, 60*60)
M,S = divmod(d, 60)

def t(n):
    if n==0:
        return("00")
    elif n<10:
        return "0"+str(n)
    else:
        return str(n)
print("{}:{}:{}".format(t(H),t(M),t(S)))
