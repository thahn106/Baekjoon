for t in range(int(input())):
    a, o, b, _, c = input().split()
    a, b, c = int(a), int(b), int(c)
    ans = False
    if o == '+':
        if a+b == c:
            ans = True
    elif o == '-':
        if a-b == c:
            ans = True
    elif o == '*':
        if a*b == c:
            ans = True
    elif o == '/':
        if a == b*c:
            ans = True
    if ans:
        print("correct")
    else:
        print("wrong answer")
