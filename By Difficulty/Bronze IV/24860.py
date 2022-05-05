V, J = map(int, input().split())
ans = V*J
V, J = map(int, input().split())
ans += V*J
V, D, J = map(int, input().split())
ans *= V*D*J
print(ans)
