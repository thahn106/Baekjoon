def leap(n):
    return n%4==0 and (n%400==0 or not(n%100==0))

months = [31,28,31,30,31,30,31,31,30,31,30,31]

D,M,Y = map(int,input().split())
while D or M or Y:
    found = False
    if 1<=M<=12:
        if M == 2 and leap(Y):
            if 1<=D<=29: found = True
        elif 1<=D<=months[M-1]: found = True
    if found: print("Valid")
    else: print("Invalid")
    D,M,Y = map(int,input().split())

