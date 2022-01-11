for t in range(int(input())):
    s = input()
    valid =True
    run = 0
    for c in s:
        if c == "(":
            run+=1
        else:
            run-=1
        if run <0:
            valid = False

    if valid and run == 0:
        print("YES")
    else:
        print("NO")
