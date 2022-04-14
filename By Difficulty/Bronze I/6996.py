for t in range(int(input())):
    a, b = input().split()
    s = ""
    if sorted(a) != sorted(b):
        s = "NOT "
    print(f"{a} & {b} are {s}anagrams.")
