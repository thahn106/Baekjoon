sol = [0 for i in range(1001)]
for i in range(1,1001):
    ans = 0
    for d in range(2,i+1):
        ni = i
        while not ni%d:
            ans+=1
            ni = ni//d
    sol[i] = ans

for t in range(int(input())):
    print(sol[int(input())])
