from math import sqrt, floor

S = int(input())
N = floor(sqrt(2*S))
if N*N+N > 2*S:
    N -= 1
print(N)
