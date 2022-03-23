N = input()
l = len(N)//2

a = sum(list(map(int,list(N[:l]))))
b = sum(list(map(int,list(N[l:]))))
if a==b:
    print("LUCKY")
else:
    print("READY")
