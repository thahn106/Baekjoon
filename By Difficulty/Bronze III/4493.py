for t in range(int(input())):
    f = 0
    s = 0
    for i in range(int(input())):
        st = input()
        if st in ["R S", "S P", "P R"]:
            f +=1
        elif st in ["S R", "P S", "R P"]:
            s +=1
    if f>s:
        print("Player 1")
    elif s>f:
        print("Player 2")
    else:
        print("TIE")
