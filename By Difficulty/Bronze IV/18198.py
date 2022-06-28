A, B = 0, 0
s = input()
n = len(s)//2
for i in range(n):
    r = int(s[2*i+1])
    if s[2*i] == 'A':
        A += r
    else:
        B += r
if A > B:
    print("A")
else:
    print("B")
