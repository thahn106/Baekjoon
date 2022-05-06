def t(n):
    if n==0:
        return("00")
    elif n<10:
        return "0"+str(n)
    else:
        return str(n)

H,M = map(int, input().split())
H1,M1 = map(int, input().split())
N = input()

ans = 0
end = False
while M!=M1 or H!=H1:
    for i in t(M)+t(H):
        if i == N:
            ans +=1
            break
    M += 1
    if M == 60:
        H += 1
        M = 0
for i in t(M)+t(H):
    if i == N:
        ans +=1
        break
print(ans)
