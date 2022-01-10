L = int(input())
H = 0
for i,c in enumerate(input()):
    H+= (ord(c)-96)*(31**i)
print(H%1234567891)
