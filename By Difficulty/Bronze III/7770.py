n = int(input())
h = 0
sum = 1
while sum <= n:
    h+=1
    sum += h**2+(h+1)**2
print(h)
