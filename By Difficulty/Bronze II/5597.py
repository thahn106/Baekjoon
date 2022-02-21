s = [1]*30
for i in range(28):
    s[int(input())-1]=0
for i in range(30):
    if s[i]:
        print(i+1)
