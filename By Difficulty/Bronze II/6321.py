for t in range(int(input())):
    ans = ""
    for c in input():
        ans += chr(((ord(c)-64)%26)+65)
    if t:
        print("")
    print(f"String #{t+1}")
    print(ans)
