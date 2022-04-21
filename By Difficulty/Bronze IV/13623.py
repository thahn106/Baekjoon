a = list(map(int, input().split()))
if sum(a) == 0 or sum(a) == 3:
    print('*')
elif sum(a) == 1:
    print('ABC'[a.index(1)])
else:
    print('ABC'[a.index(0)])
