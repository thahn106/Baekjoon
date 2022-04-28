min = 1000000000000000000
minn = ""
max = 0
maxn = ""

months = [31,29,31,30,31,30,31,31,30,31,30,31]

for i in range(int(input())):
    name,d,m,y = input().split()
    date = int(y)*366+sum(months[:int(m)-1])+int(d)
    if date<min:
        minn = name
        min = date
    if date>max:
        maxn = name
        max = date

print(maxn)
print(minn)
