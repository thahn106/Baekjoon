N = list(input())
c = [0]*10
for d in N:
    c[int(d)]+=1

d = (c[6]+c[9]+1)//2
c[6]=d
c[9]=d
print(max(c))
