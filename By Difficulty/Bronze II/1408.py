def t(n):
    if n==0:
        return("00")
    elif n<10:
        return "0"+str(n)
    else:
        return str(n)


H,M,S = map(int,input().split(":"))
H1,M1,S1 = map(int,input().split(":"))
T = ((H1-H)*3600+(M1-M)*60+(S1-S))%(24*60*60)
H,T = divmod(T,3600)
M,S = divmod(T,60)
print("{}:{}:{}".format(t(H),t(M),t(S)))
