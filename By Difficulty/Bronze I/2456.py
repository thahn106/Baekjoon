score = [0, 0, 0]
thr = [0, 0, 0]
two = [0, 0, 0]
for n in range(int(input())):
    a = list(map(int, input().split()))
    for i, c in enumerate(a):
        score[i] += c
        if c == 2:
            two[i] += 1
        elif c == 3:
            thr[i] += 1
lead = []
for i in range(3):
    lead.append((score[i], thr[i], two[i], i+1))

lead.sort(reverse=True)
if lead[0][:3] == lead[1][:3]:
    print(0, lead[0][0])
else:
    print(lead[0][3], lead[0][0])
