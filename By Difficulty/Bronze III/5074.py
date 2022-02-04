def t(n):
    if n==0:
        return("00")
    elif n<10:
        return "0"+str(n)
    else:
        return str(n)

s = input()
while s != "00:00 00:00":
    st,d = s.split()
    sh,sm = map(int,st.split(":"))
    dh,dm = map(int,d.split(":"))
    T = sh*60+sm+dh*60+dm
    D,T = divmod(T,24*60)
    H,M = divmod(T,60)
    ans = t(H)+":"+t(M)
    if D:
        ans += " +"+str(D)
    print(ans)
    s = input()
