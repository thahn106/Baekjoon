mods = [0 for i in range(42)]
for i in range(10):
    mods[int(input())%42] = 1
print(sum(mods))
