t1,m1,t2,m2 = map(int,input().split())
t = ( (t2-t1)*60 + m2-m1) % (24*60)
print(t, t//30)
