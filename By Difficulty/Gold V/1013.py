def check(str):
    if not str:
        return True
    else:
        i = len(str)-1
        ones = 0
        zeroes = 0
        while i>=0 and str[i]=='1':
            ones +=1
            i-=1
        while i>=0 and str[i]=='0':
            zeroes +=1
            i-=1
        if i>=0 and str[i] == '1' and zeroes>=2 and ones >=1:
            return check(str[:i])
        else:
            return False

for t in range(int(input())):
    strlist = []
    s = input()
    working = True
    i=0
    while working:
        found = False
        if s[i]=='0' and i < len(s)-1 and s[i+1]=='1':
            if i!=0:
                if s[i-1]=='1':
                    found = True
            else:
                found = True
        if found:
            strlist.append(s[:i])
            s = s[i+2:]
            i=0
        else:
            i+=1
        if not s or i >= len(s):
            working=False
    if s:
        strlist.append(s)
    possible = True
    for str in strlist:
        if not check(str):
            possible=False
    if possible:
        print("YES")
    else:
        print("NO")
