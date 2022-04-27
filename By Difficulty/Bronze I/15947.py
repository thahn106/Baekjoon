d, r = divmod(int(input())-1, 14)
if r == 0 or r == 12:
    print('baby')
elif r == 1 or r == 13:
    print('sukhwan')
elif r == 2 or r == 6 or r == 10:
    if d >= 3:
        print(f"tu+ru*{(d+2)}")
    else:
        print(f"tu{'ru'*(d+2)}")
elif r == 3 or r == 7 or r == 11:
    if d >= 4:
        print(f"tu+ru*{(d+1)}")
    else:
        print(f"tu{'ru'*(d+1)}")
elif r == 4:
    print('very')
elif r == 5:
    print('cute')
elif r == 8:
    print('in')
elif r == 9:
    print('bed')
else:
    print(-1)
