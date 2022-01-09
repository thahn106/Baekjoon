H,M = map(int,input().split())
M -= 45
H -= M<0
print("{} {}".format(H%24,M%60))
