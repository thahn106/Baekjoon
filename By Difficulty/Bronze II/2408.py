from math import floor
N = int(input())
ans = []
top = int(input())
sign = 1
for i in range(N-1):
    op = input()
    d = int(input())
    if op == "+":
        ans.append(top*sign)
        top = d
        sign = 1
    elif op == "-":
        ans.append(top*sign)
        top = d
        sign = -1
    elif op == "*":
        top *=d
    else:
        top = top//d
ans.append(top*sign)
print(sum(ans))
