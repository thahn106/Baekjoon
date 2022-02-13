for t in range(int(input())):
    creds = 0
    gpa = 0
    for n in range(int(input())):
        c,g = input().split()
        creds += int(c)
        gpa += int(c)*float(g)
    print("{} {}".format(creds, gpa/creds))
