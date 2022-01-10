N = input()

def p10 (x):
    i =0
    while x%10==0:
        x = x//10
        i+=1
    return (x==1), i

def digits(nstr, leading):
    # print("{} {}".format(nstr,leading))
    first = int(nstr[0])
    rest = nstr[1:]
    x = int(nstr)

    ans = [0 for i in range(10)]
    p,e = p10(x+1)
    if p and e:
        ans = [e*(10**(e-1)) for i in range(10)]
        if not leading:
            for i in range(e):
                ans[0] -= 10**i
        return ans
    if len(nstr)<2:
        ans = [0 for i in range(10)]
        for i in range(1-int(leading),x+1):
            ans[i] = 1
        return ans
    else:
        n = str(x)
        for i in range(0,first):
            if i!=0 or leading:
                ta = digits(str(10**(len(n)-1)-1), True)
                ta[i]+= 10**(len(n)-1)
            else:
                ta = digits(str(10**(len(n)-1)-1), leading)
            for dig in range(10):
                ans[dig]+=ta[dig]
        ans[first]+= (int(rest)+1)
        ta = digits(rest, True)
        for dig in range(10):
            ans[dig]+=ta[dig]
        return ans

print(*digits(N, False))
