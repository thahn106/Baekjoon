for t in range(int(input())):
    h, w = map(int, input().split())
    bmi = 10000*w/(h*h)
    if h <= 140:
        print(6)
    elif h < 146:
        print(5)
    elif h < 159:
        print(4)
    elif h < 161:
        if 16 <= bmi < 35:
            print(3)
        else:
            print(4)
    elif h < 204:
        if 20 <= bmi < 25:
            print(1)
        elif 18.5 <= bmi < 30:
            print(2)
        elif 16 <= bmi < 35:
            print(3)
        else:
            print(4)
    else:
        print(4)
