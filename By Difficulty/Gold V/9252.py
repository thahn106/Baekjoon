import sys
import time

L = 1000

# sa = "A"*L
# sb = "A"*L

sa = input()
sb = input()
a = len(sa)
b = len(sb)


starttime = time.time()
prevrow = ["" for i in range(a+1)]

for bi,bc in enumerate(sb):
    row = ["" for i in range(a+1)]
    for ai,ac in enumerate(sa):
        if ac == bc:
            row[ai+1]=prevrow[ai]+ac
        else:
            s1 = prevrow[ai+1]
            s2 = row[ai]
            if len(s1)<len(s2):
                row[ai+1]=s2
            else:
                row[ai+1]=s1
    prevrow = row

# print(sys.getsizeof(prevrow))
s = len(prevrow[-1])

print(s)
if s:
    print(prevrow[-1])
# print("Time elapsed:{}".format(time.time()-starttime))
