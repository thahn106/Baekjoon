a, x, b, y, T = [int(input()) for i in range(5)]

A = a + 21*max(T-30, 0)*x
B = b + 21*max(T-45, 0)*y
print(A, B)
