n,a,w = input().split()
while n!='#':
    if int(a)>17 or int(w)>=80:
        div = "Senior"
    else:
        div = "Junior"
    print("{} {}".format(n,div))
    n,a,w = input().split()
