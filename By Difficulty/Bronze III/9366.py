for t in range(int(input())):
    a = list(map(int,input().split()))
    a.sort()
    if a[0]+a[1]<=a[2]:
        ans = "invalid!"
    elif a[0]==a[2]:
        ans = 'equilateral'
    elif a[0]==a[1] or a[1]==a[2]:
        ans = 'isosceles'
    else:
        ans = 'scalene'
    print(f"Case #{t+1}: {ans}")
