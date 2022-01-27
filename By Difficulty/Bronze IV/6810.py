ref = [9,7,8,0,9,2,1,4,1,8]
for i in range(3):
    ref.append(int(input()))
ans = 0
for i in range(13):
    ans += ref[i]*((i%2)*2+1)
print("The 1-3-sum is {}".format(ans))
