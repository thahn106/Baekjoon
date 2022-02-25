found = False
ans = []
for i in range(1,6):
    if "FBI" in input():
        ans.append(i)
        found = True
if found:
    print(*ans)
else:
    print("HE GOT AWAY!")
