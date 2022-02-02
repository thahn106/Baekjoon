a,b = input().split()
while int(a) or int(b):
    ans = 0
    carry = 0
    for i in range(max(len(a),len(b))):
        x = 0
        y = 0
        if i<len(a):
            x=int(a[-(i+1)])
        if i<len(b):
            y=int(b[-(i+1)])
        carry  = int(x+y+carry>=10)
        ans += carry
    print(ans)
    a,b = input().split()
