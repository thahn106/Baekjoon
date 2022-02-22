from itertools import permutations
N = int(input())
a = list(map(int,input().split()))
ans = 0
for num in permutations(a):
    count = 0
    for i in range(N):
        ind=i
        run = 0
        while run<50:
            run+=num[ind]
            ind = (ind+1)%N
        if run==50:
            count+=1
    # print(f"{num = }")
    # print(f"{count = }")
    ans = max(ans,count//2)
print(ans)
