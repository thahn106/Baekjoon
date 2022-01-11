import sys
input = sys.stdin.buffer.readline

K = int(input())
nums = [0 for i in range(K)]
j = 0
for i in range(K):
    n = int(input())
    if n:
        nums[j] = n
        j+=1
    else:
        j-=1
        nums[j] = 0

print(sum(nums))
