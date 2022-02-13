lab = ["Q1","Q2","Q3","Q4","AXIS"]
q = [0]*5
for n in range(int(input())):
    x,y = map(int,input().split())
    if x == 0 or y == 0:
        q[4]+=1
    else:
        if x>0:
            if y>0:
                q[0]+=1
            else:
                q[3]+=1
        else:
            if y>0:
                q[1]+=1
            else:
                q[2]+=1

for i in range(5):
    print("{}: {}".format(lab[i],q[i]))
