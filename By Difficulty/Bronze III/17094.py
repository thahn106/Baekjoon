input()
e = 0
for c in input():
    if c == 'e':
        e += 1
    else:
        e -= 1
if e>0:
    print("e")
elif e<0:
    print("2")
else:
    print("yee")
