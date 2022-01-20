sa = input()
sb = input()
a = len(sa)
b = len(sb)

prevrow = ["" for i in range(a+1)]

for bi,bc in enumerate(sb):
    row = [""]
    for ai,ac in enumerate(sa):
        if ac == bc:
            row.append(prevrow[ai]+ac)
        else:
            s1 = prevrow[ai+1]
            s2 = row[-1]
            if len(s1)<len(s2):
                row.append(s2)
            else:
                row.append(s1)
    prevrow = row

s = len(prevrow[-1])
print(s)
