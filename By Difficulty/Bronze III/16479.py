K = int(input())
a,b = map(int,input().split())
a,b = min(a,b), max(a,b)
print((K**2-((b-a)/2)**2))
