cur = int(input())-1
N = int(input())
time = 0
for i in range(N):
    t,a = input().split()
    time+=int(t)
    if time>=210:
        break
    if a == 'T':
        cur = (cur+1)%8
print(cur+1)
