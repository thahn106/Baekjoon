from math import ceil
t = 0
s = int(input())
while s:
    ans = ceil(ceil(3*ceil(s/2)/2) / (62*30000))
    if t:
        print("")
    print(f"File #{t+1}")
    print(f"John needs {ans} floppies.")
    t += 1
    s = int(input())
