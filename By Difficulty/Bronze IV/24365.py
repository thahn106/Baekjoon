A,B,C = map(int, input().split())
S = (A+B+C)//3
ans = 0
ans += abs(S-A)
B += (A-S)
ans += abs(S-B)
print(ans)
