a = input()
twos = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
ans = 0
i = 0
while i < len(a):
    ans +=1
    if a[i:i+2] in twos:
        i+=2
    elif a[i:i+3]=='dz=':
        i+=3
    else:
        i+=1
print(ans)
