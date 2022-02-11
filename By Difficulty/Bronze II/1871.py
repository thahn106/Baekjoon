for t in range(int(input())):
    s,t = input().split('-')
    S = 26*26*(ord(s[0])-65)+26*(ord(s[1])-65)+(ord(s[2])-65)
    T = int(t)
    if abs(S-T)<=100:
        print("nice")
    else:
        print("not nice")
