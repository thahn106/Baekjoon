N = int(input())
F = int(input())
if N%100 >= N%F:
    N -= N%F
else:
    N += (F-(N%F))
while N%100 >= F:
    N-=F
print(str(N)[-2:])
