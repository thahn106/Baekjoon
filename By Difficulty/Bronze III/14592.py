ans,S,C,L = 0,0,51,180
for i in range(int(input())):
    s,c,l = map(int,input().split())
    if s>S or (s==S and (c<C or (c==C and l<L))):
        ans,S,C,L = i+1,s,c,l
print(ans)
