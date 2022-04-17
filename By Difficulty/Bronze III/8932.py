from math import floor
type = [1, -1, -1, 1, -1, -1, 1]
A = [9.23076, 1.84523, 56.0211, 4.99087, 0.188807, 15.9803, 0.11193]
B = [26.7, 75, 1.5, 42.5, 210, 3.8, 254]
C = [1.835, 1.348, 1.05, 1.81, 1.41, 1.04, 1.88]
for t in range(int(input())):
    P = list(map(int, input().split()))
    ans = 0
    for i, p in enumerate(P):
        ans += floor(A[i]*pow(type[i]*(B[i]-p), C[i]))
    print(ans)
