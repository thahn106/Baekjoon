s = input()
ans = ""
if s[0]=="E":
    ans += "I"
else:
    ans += "E"
if s[1]=="S":
    ans += "N"
else:
    ans += "S"
if s[2]=="T":
    ans += "F"
else:
    ans += "T"
if s[3]=="J":
    ans += "P"
else:
    ans += "J"
print(ans)
