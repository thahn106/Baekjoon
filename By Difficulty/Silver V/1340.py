monthstr = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
months = [31,28,31,30,31,30,31,31,30,31,30,31]
def leap(n):
    return n%4==0 and (n%400==0 or not(n%100==0))

time = input().split()
month = monthstr.index(time[0])
day = int(time[1][:-1])
year = int(time[2])
H,M = map(int,time[3].split(':'))

total = 365*24*60
if leap(year):
    total+=24*60

ans = 0
m = 0
while m<month:
    ans += months[m]*24*60
    if m == 1 and leap(year):
        ans += 24*60
    m+=1
ans += (day-1)*24*60
ans += H*60+M
print(100*ans/total)
