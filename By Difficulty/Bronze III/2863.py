A,B = map(int,input().split())
C,D = map(int,input().split())
ans = []
ans.append(A/C + B/D)
ans.append(C/D + A/B)
ans.append(D/B + C/A)
ans.append(B/A + D/C)

for i in range(4):
    if ans[i] == max(ans):
        print(i)
        break
