from math import floor
N = int(input())
calls = list(map(int,input().split()))
Y, M = 0, 0
for call in calls:
    Y += (floor(call/30)+1)*10
    M += (floor(call/60)+1)*15

if Y<M:
    print("Y {}".format(Y))
elif Y == M:
    print("Y M {}".format(Y))
else:
    print("M {}".format(M))
