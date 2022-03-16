ref = '22233344455566677778889999'
for i in range(int(input())):
    s = input().upper()
    ans = ""
    for c in s:
        ans += ref[ord(c)-65]

    if ans==ans[::-1]:
        print("YES")
    else:
        print("NO")
