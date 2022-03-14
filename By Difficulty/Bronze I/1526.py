n = input()
l = len(n)
N = int(n)
found = False
for i in range(2**l):
    ans = ""
    x = bin(i)[2:]
    s = '0'*(l-len(x))+x
    for c in s:
        if c == '0':
            ans +='7'
        else:
            ans +='4'
    if int(ans)<=N:
        found = True
        print(ans)
        break
if not found:
    print('7'*(l-1))
