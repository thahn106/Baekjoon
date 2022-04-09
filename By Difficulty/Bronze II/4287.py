N = input()
while N != '#':
    a,b,s = N.split()
    ans = ""
    for i,c in enumerate(s):
        ans += chr((ord(b[i])-ord(a[i])+ord(s[i])-97)%26+97)
    print(a,b,s,ans)
    N = input()
