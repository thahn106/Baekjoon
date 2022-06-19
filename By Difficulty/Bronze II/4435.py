for t in range(int(input())):
    a = list(map(int, input().split()))
    A = 0
    for x,y in zip(a,[1,2,3,3,4,10]):
        A += x*y
    a = list(map(int, input().split()))
    B = 0
    for x,y in zip(a,[1,2,2,2,3,5,10]):
        B += x*y
    if A>B:
        ans = "Good triumphs over Evil"
    elif B>A:
        ans = "Evil eradicates all trace of Good"
    else:
        ans = "No victor on this battle field"
    print(f"Battle {t+1}: {ans}")
