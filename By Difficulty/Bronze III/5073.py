a = sorted(list(map(int,input().split())))
while a[0] or a[2]:
    if a[0]+a[1]<=a[2]:
        print("Invalid")
    elif a[0]==a[2]:
        print("Equilateral")
    elif a[0]==a[1] or a[2]==a[1]:
        print("Isosceles")
    else:
        print("Scalene")
    a = sorted(list(map(int,input().split())))
