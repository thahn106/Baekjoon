T = int(input())
ans = []
while T:
    T,r = divmod(T,9)
    ans.append(str(r))
ans.reverse()
print("".join(ans))
