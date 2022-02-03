f = float(input())
while True:
    n = float(input())
    if int(n)==999:
        break
    print("{:.2f}".format(n-f))
    f = n
    
