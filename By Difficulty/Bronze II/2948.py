D,M = map(int,input().split())
months = [31,28,31,30,31,30,31,31,30,31,30,31]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
i = (sum(months[:(M-1)])+D+2)%7
print(days[i])
