ans = 0
try:
    while True:
        n = input()
        ans += 1
except EOFError as e:
    print(ans)
