for t in range(int(input())):
    n,s = input().split()
    if s == 'kg':
        print(f"{round(float(n)*2.2046,4):.4f} lb")
    elif s == 'lb':
        print(f"{round(float(n)*0.4536,4):.4f} kg")
    elif s == 'g':
        print(f"{round(float(n)*3.7854,4):.4f} l")
    else:
        print(f"{round(float(n)*0.2642,4):.4f} g")
