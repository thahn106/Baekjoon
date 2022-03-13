s = list(map(int,(list(input()))))

valid = False
if len(s)>=2:
    for i in range(1,len(s)):
        A = 1
        B = 1
        for a in s[:i]:
            A*=a
        for b in s[i:]:
            B*=b
        if A == B:
            valid=True
            break


if valid:
    print("YES")
else:
    print("NO")
