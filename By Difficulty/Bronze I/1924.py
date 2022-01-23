days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
months = [31,28,31,30,31,30,31,31,30,31,30,31]

x,y = map(int,input().split())
day = sum(months[:x-1])+y
print(days[day%7])
