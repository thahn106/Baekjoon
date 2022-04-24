n = int(input())
a = list(input())
b = list(input())
working = True

for x, y in zip(a, b):
    if n%2 ^ (x!=y):
        working = False
if working:
    print("Deletion succeeded")
else:
    print("Deletion failed")
