from math import sqrt, floor,ceil

def is_square(n):
    return floor(sqrt(n))==sqrt(n)

N,M = map(int,input().split())
board = []
for i in range(N):
    board.append(input())

ans = -1
l = max(N,M)
while l > 0:
    for n in range(N):
        for m in range(M):
            if l == 1:
                num = int(board[n][m])
                if is_square(num):
                    ans = max(ans, num)
            else:
                for dy in range(ceil(-n/(l-1)),floor((N-1-n)/(l-1))+1):
                    for dx in range(ceil(-m/(l-1)),floor((M-1-m)/(l-1))+1):
                        if not ((dx==0 and dy ==0)):
                            temp = []
                            for i in range(l):
                                temp.append(board[n+dy*i][m+dx*i])
                            num = int("".join(temp))
                            if is_square(num):
                                ans = max(ans, num)
                                # print("l:{} n:{} m:{} dy:{}, dx:{}".format(l,n,m,dy,dx))
    l-=1

print(ans)
