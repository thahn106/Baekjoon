S = input()
N = int(input())
words = []
for n in range(N):
    words.append(input())
    
dp = {}
def cost(x,y):
    if (x,y) in dp:
        return dp[(x,y)]
    else:
        # print("x:{} y:{}".format(x,y))
        s = S[x:y]
        ans = -1
        for word in words:
            if len(word) == len(s):
                tw = list(word)
                tw.sort()
                ts = list(s)
                ts.sort()
                if tw == ts:
                    ta = 0
                    for i in range(len(s)):
                        if word[i]!=s[i]:
                            ta += 1
                    if ans != -1:
                        ans = min(ans,ta)
                    else:
                        ans = ta
        for i in range(x+1,y):
            a,b = cost(x,i),cost(i,y)
            if a!=-1 and b != -1:
                if ans != -1:
                    ans = min(ans,a+b)
                else:
                    ans = a+b
        dp[(x,y)] = ans
        return ans

print(cost(0,len(S)))
