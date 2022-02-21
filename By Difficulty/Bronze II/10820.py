try:
    while True:
        s = input()
        ans = [0,0,0,0]
        for c in s:
            if c == ' ':
                ans[3]+=1
            elif 65<=ord(c)<=90:
                ans[1]+=1
            elif 97<=ord(c)<=122:
                ans[0]+=1
            elif 48<=ord(c)<=57:
                ans[2]+=1
        print(*ans)
except EOFError as e:
    pass
