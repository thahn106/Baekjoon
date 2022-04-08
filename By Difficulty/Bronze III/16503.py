def op(m,n,o):
    if o=='+':
        return m+n
    elif o == '-':
        return m-n
    elif o == '*':
        return m*n
    else:
        if m*n < 0:
            sign = -1
        else:
            sign = 1
        return sign*(abs(m)//abs(n))
a,o,b,p,c = input().split()
a,b,c = int(a),int(b),int(c)
m = op(a,op(b,c,p),o)
n = op(op(a,b,o),c,p)
print(min(m,n))
print(max(m,n))
