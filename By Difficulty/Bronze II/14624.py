N = int(input())
if N%2:
    print('*'*N)
    d = N//2
    print(' '*d+'*')
    for i in range(d):
        print(' '*(d-1-i)+'*'+' '*(2*i+1)+'*')
else:
    print("I LOVE CBNU")
