X = int(input())
for n in range(int(input())):
    a, b = map(int, input().split())
    X -= a*b
if X == 0:
    print("Yes")
else:
    print("No")
