N,C = map(int,input().split())
p =[int(input()) for i in range(N)]
cc = [0 for i in range(C+1)]
for c in p:
    j = 1
    while j*c<= C:
        cc[j*c] = 1
        j+=1
print(sum(cc))
