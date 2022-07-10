s = list(map(int, input().split()))
if s == sorted(s):
    print("Good")
else:
    print("Bad")
