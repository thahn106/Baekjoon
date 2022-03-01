N = int(input(),2)
li = []
while N:
    N,r = divmod(N,8)
    li.append(str(r))

li.reverse()
print("".join(li))
