a = []
for i in range(4):
    a.append(int(input()))
if min(a)==max(a):
    print("Fish At Constant Depth")
elif a[0]<a[1]<a[2]<a[3]:
    print("Fish Rising")
elif a[0]>a[1]>a[2]>a[3]:
    print("Fish Diving")
else:
    print("No Fish")
