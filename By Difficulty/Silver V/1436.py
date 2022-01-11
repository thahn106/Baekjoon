N = int(input())
nums = set()
nums.add(666)

for i in range(1,5):
    for j in range(i+1):
        before = j
        after = i-j
        base = 666*(10**(after))
        for b in range(10**before):
            for a in range(10**after):
                nums.add(b*(10**(after+3))+base+a)
nums = list(nums)
nums.sort()
print(nums[N-1])
