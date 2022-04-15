a, b = 0, 1
for n in range(int(input())):
    a, b = b, a+b
print(2*(a+b))
