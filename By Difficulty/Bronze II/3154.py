H,M = map(int,input().split(':'))

coords = [(3,1)]
for i in range(9):
    coords.append((i//3,i%3))

def t(n):
    if n==0:
        return("00")
    elif n<10:
        return "0"+str(n)
    else:
        return str(n)

effort = 1000
ans = ""
while H<100:
    m = M
    while m<100:
        ref = t(H)+t(m)
        temp = 0
        for i in range(3):
            xa,ya = coords[int(ref[i])]
            xb,yb = coords[int(ref[i+1])]
            temp += abs(xa-xb)+abs(ya-yb)
        if temp < effort:
            effort = temp
            ans = f"{t(H)}:{t(m)}"

        m+=60
    H+=24

print(ans)