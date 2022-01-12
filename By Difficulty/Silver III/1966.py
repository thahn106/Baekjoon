for t in range(int(input())):
    N,M = map(int,input().split())
    nums = list(map(int,input().split()))
    ind = list(range(N))
    ans = []
    while nums:
        n = nums.pop(0)
        i = ind.pop(0)
        if (not nums) or n >= max(nums):
            ans.append(i)
        else:
            nums.append(n)
            ind.append(i)
    print(ans.index(M)+1)
