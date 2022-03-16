s = input()
while s != '0':
    k,m = map(int,s.split())
    taken = [False]*10000
    for course in input().split():
        taken[int(course)]=True
    grad = True
    for M in range(m):
        a = list(map(int,input().split()))
        c = int(a[0])
        r = int(a[1])
        count = 0
        for course in a[2:]:
            if taken[int(course)]:
                count += 1
        if count < r:
            grad = False
        # print(f"cat {M}: {count}")
    if grad:
        print("yes")
    else:
        print("no")
    s = input()
