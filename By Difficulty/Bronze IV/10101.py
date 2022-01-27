a = [int(input()) for i in range(3)]
a.sort()
if sum(a)!=180:
    print("Error")
elif a[0]==a[2]:
    print("Equilateral")
elif a[0]==a[1] or a[2]==a[1]:
    print("Isosceles")
else:
    print("Scalene")
