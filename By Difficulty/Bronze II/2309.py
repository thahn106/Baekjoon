A = [int(input()) for i in range(9)]
A.sort()
def find(a):
    for i in range(8):
        for j in range(i+1,9):
            if sum(a)-a[i]-a[j]==100:
                for k in range(9):
                    if k!=i and k!=j:
                        print(a[k])
                return 0
find(A)
