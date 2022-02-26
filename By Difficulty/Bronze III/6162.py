from math import ceil
for k in range(int(input())):
    E,A = map(int,input().split())

    d = 0
    while E > A:
        A*=5
        d+=1
    if k:
        print("")
    print(f"Data Set {k+1}:")
    if not d:
        print("no drought")
    else:
        print("mega "*(d-1)+"drought")
