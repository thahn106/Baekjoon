from math import ceil
s = input()

l = len(s)
for i in range(ceil(l/10)):
    print(s[10*i:10*i+10])
