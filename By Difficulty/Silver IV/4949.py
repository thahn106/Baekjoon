s = input()
while s != ".":
    paren = []
    valid = True
    a = 0
    b = 0
    for c in s:
        if c == "(":
            paren.append(0)
            a +=1
        elif c == ")":
            if a and  paren[-1] == 0:
                paren.pop()
                a -= 1
            else:
                valid = False
                break
        elif c == "[":
            paren.append(1)
            b+=1
        elif c == "]":
            if b and paren[-1] == 1:
                paren.pop()
                b-=1
            else:
                valid = False
                break
    if valid and not paren:
        print("yes")
    else:
        print("no")
    s = input()
