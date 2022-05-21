N = int(input())
grid = []
for i in range(N):
    s = ""
    for j in range(5):
        s+= input()
    grid.append(s)

ans = 36
A,B = 0,0
for i in range(N-1):
    for j in range(i+1,N):
        temp = 0
        for a,b in zip(grid[i],grid[j]):
            if a!=b:
                temp +=1
        if temp < ans:
            ans = temp
            A,B = i+1,j+1
print(A,B)
