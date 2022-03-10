def rps(x,y):
    if x == y:
        return 0
    elif x+y in ["RP","PS","SR"]:
        return 1
    else:
        return -1

a,b,c,d = input().split()

win = [rps(a,c),rps(a,d),rps(b,c),rps(b,d)]
if win[0]==win[1]==-1 or win[2]==win[3]==-1:
    print("MS")
elif win[0]==win[2]==1 or win[1]==win[3]==1:
    print("TK")
else:
    print("?")
