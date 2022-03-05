key = input()
while key != '0':
    message = input()
    ans = ""
    for i, c in enumerate(message):
        a = ((ord(c)-64)+(ord(key[i % len(key)])-64)) % 26
        if not a:
            a = 26
        ans += chr(a+64)
    print(ans)
    key = input()
