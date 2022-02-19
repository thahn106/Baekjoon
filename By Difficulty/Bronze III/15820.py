s1,s2 = map(int,input().split())
sr = True
for i in range(s1):
    a,b = map(int,input().split())
    if a!=b:
        sr = False
fr = True
for i in range(s2):
    a,b = map(int,input().split())
    if a!=b:
        fr = False

if sr and fr:
    print("Accepted")
elif sr:
    print("Why Wrong!!!")
else:
    print("Wrong Answer")
