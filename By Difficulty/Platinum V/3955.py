from math import gcd

for t in range(int(input())):
    K, C = map(int, input().split())
    if gcd(K, C) != 1:
        print('IMPOSSIBLE')
    else:
        ans = pow(C, -1, K)
        if C == 1:
            ans = K+1
        if ans*C <= K:
            ans += K
        if ans > 10**9:
            print('IMPOSSIBLE')
        else:
            print(ans)
