s = input()
while s !='END':
    x0 = int(s)
    if x0==1:
        print(1)
    elif len(s)==1:
        print(2)
    elif len(s)<10:
        print(3)
    else:
        print(4)
    s = input()
