n = int(input())
s = input()
ref = ["000000", "001111", "010011", "011100", "100110", "101001", "110101", "111010"]
ans = ""
wrong = False
for i in range(n):
    temp = ""
    c = s[6*i:6*i+6]
    r = []
    for j in range(8):
        count = 0
        for a,b in zip(ref[j],c):
            if a!=b:
                count+=1
        r.append(count)
        if count<2:
            temp+=chr(j+65)
    if min(r)>=2:
        print(i+1)
        wrong = True
        break
    if len(temp)==1:
        ans+=temp
if not wrong:
    print(ans)
