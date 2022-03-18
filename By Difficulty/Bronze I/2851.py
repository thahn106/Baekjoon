ans = 0
run = 0
for i in range(10):
    run +=int(input())
    if abs(100-ans)>=abs(100-run):
        ans = run
print(ans)
