N,B =input().split()
B = int(B)
num = list(N)
num.reverse()
ans = 0
for i,d in enumerate(num):
    if ord(d)>=65:
        d = ord(d)-55
    else:
        d = int(d)
    ans+= d*B**i
print(ans)
