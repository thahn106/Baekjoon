N =int(input())
a = list(map(int,input().split()))
sum = 0
for i in a:
    sum += i*100/max(a)
print(sum/N)
