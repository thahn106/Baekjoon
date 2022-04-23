N = int(input())
K = int(input())
if N > 5:
    print("Love is open door")
else:
    for i in range(N-1):
        K = 1-K
        print(K)
