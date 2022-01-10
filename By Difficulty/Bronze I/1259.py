s = input()
while int(s):
    if s == s[::-1]:
        print("yes")
    else:
        print("no")
    s = input()
