vowels = list("AEIOUaeiou")
s = input()

while s !="#":
    ans = 0
    for c in s:
        if c in vowels:
            ans +=1
    print(ans)
    s = input()
