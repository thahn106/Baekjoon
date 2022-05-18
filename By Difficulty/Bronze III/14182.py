n = int(input())
while n:
    if n>5000000:
        print(n*4//5)
    elif n>1000000:
        print(n*9//10)
    else:
        print(n)
    n = int(input())
