import sys
input = sys.stdin.buffer.readline

S = [0 for i in range(20)]
j=0
for i in range(int(input())):
    s= [str(i,'utf-8') for i in input().strip().split()]
    if s[0] == "empty":
        S = [0 for i in range(20)]
    elif s[0] == "all":
        S = [1 for i in range(20)]
    elif s[0] == "toggle":
        S[int(s[1])-1] = 1-S[int(s[1])-1]
    elif s[0] == "check":
        sys.stdout.write(str(S[int(s[1])-1]) + "\n")
        j+=1
        if j%1000==0:
            sys.stdout.flush()
    elif s[0] == "remove":
        S[int(s[1])-1] = 0
    elif s[0] == "add":
        S[int(s[1])-1] = 1

sys.stdout.flush()
