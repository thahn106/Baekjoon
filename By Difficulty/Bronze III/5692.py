import sys
fac = [1,2,6,24,120,720]
while True:
    n = sys.stdin.readline().strip()
    if n == "0":
        break
    ans = 0
    for i in range(len(n)):
        ans += fac[i]*int(n[-(i+1)])
    sys.stdout.write(str(ans)+"\n")

sys.stdout.flush()
