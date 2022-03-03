for t in range(int(input())):
    count = [65+i for i in range(26)]
    for c in input():
        count[ord(c)-65] = 0
    print(sum(count))
