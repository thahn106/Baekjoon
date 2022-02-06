Y,M,D = map(int,input().split())
Y1,M1,D1 = map(int,input().split())

year = Y1-Y
het =  year+1
man = year-1+(M1>M or (M1==M and D1>=D))

print(man)
print(het)
print(year)
