n = list(map(int,input().split()))
up, down = False, False
for i in range(1,8):
    if n[i]>n[i-1]:
        up = True
    elif n[i]<n[i-1]:
        down = True
if up and down:
    print("mixed")
elif up:
    print("ascending")
elif down:
    print("descending")
else:
    print("ERROR")
