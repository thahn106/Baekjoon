N = int(input())

nums = [i+1 for i in range(N)]
nn = []
ind = 0
for i in range(N-1):
    ind +=1
    if ind == len(nums):
        nums = nn
        ind =0
        nn = []
    nn.append(nums[ind])
    ind +=1
    if ind == len(nums):
        nums = nn
        ind =0
        nn = []
print(*nums)
