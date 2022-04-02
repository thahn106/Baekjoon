for n in range(int(input())):
    s,t = input().split()
    if sorted(list(s))==sorted(list(t)):
        print("Possible")
    else:
        print("Impossible")
