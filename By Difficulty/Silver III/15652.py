N,M = map(int,input().split())

def pick(start,end, nums, count):
    for i in range(start,end+1):
        nl = nums.copy()
        nl.append(i)
        if count>1:
            pick(i,end, nl.copy(),count-1)
        else:
            print(*nl)

pick(1,N,[],M)
