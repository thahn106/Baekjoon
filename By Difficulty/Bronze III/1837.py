P,K = map(int,input().split())
good = True
p = 1
for i in range(2,K):
    if P%i==0:
        good = False
        print("BAD {}".format(i))
        break
if good:
    print("GOOD")
