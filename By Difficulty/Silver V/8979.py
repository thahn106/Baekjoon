N,K = map(int,input().split())

countries = []
for i in range(N):
    c,g,s,b = map(int,input().split())
    countries.append((g,s,b,c))

countries.sort(reverse=True)
places = [0]*N

ref = 0
curplace = 1
for i,c in enumerate(countries):
    if ref != c[:-1]:
        curplace = i+1
        ref = c[:-1]
    places[c[3]-1]=curplace
print(places[K-1])
