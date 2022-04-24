print('n e')
print('- -----------')
print('''0 1
1 2
2 2.5
3 2.666666667
4 2.708333333''')
e = 0
fac = 1

for n in range(10):
    if n:
        fac *= n
    e += 1/fac
    if n>4:
        print(f"{n} {e:.9f}")
