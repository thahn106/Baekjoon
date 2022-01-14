P = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for i in range(10,101):
    P.append(P[i-1]+P[i-5])

for t in range(int(input())):
    print(P[int(input())-1])
