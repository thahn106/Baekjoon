for t in range(int(input())):
    if t:
        print("")
    n = int(input())
    for i in range(n):
        if i == 0 or i == n-1:
            print("#"*n)
        else:
            print("#"+"J"*(n-2)+"#")
