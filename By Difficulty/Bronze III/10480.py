for n in range(int(input())):
    x = int(input())
    if x%2:
        ans = "odd"
    else:
        ans = "even"
    print(f"{x} is {ans}")
