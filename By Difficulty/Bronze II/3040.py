ans = []
for i in range(9):
    ans.append(int(input()))

s = sum(ans)
for i in range(8):
    for j in range(i+1,9):
        if s-ans[i]-ans[j]==100:
            l=ans[i]
            r=ans[j]
            ans.remove(l)
            ans.remove(r)
            for c in ans:
                print(c)
            exit()
