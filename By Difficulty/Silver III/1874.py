n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

possible = True
ans = []
stack = []
m = 0
for i in nums:
    while i>m:
        m+=1
        stack.append(m)
        ans.append('+')
    if stack and stack[-1] == i:
        stack.pop()
        ans.append('-')
    else:
        possible = False
        break

if possible:
    for i in ans:
        print(i)
else:
    print("NO")
