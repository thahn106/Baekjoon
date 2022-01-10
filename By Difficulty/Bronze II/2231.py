N=int(input())
found = False
for n in range(max(0,N-63),N+1):
    if N == n+sum([int(c) for c in str(n)]):
        print(n)
        found =True
        break
if not found:
    print(0)
