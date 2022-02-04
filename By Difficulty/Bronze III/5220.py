for t in range(int(input())):
    s, b = map(int,input().split())
    s = list(map(int, list(bin(s)[2:])))
    if (sum(s)-b)%2:
        print("Corrupt")
    else:
        print("Valid")
