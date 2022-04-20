gd = {
    'A+': 4.3,
    'A0': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B0': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C0': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D0': 1.0,
    'D-': 0.7,
    'F': 0.0
}
credits = 0
gpa = 0
for t in range(int(input())):
    n, c, g = input().split()
    c = int(c)
    credits += c
    gpa += c*gd[g]
q, r = divmod(1000*gpa/credits, 10)
if r >= 5:
    q += 1


def t(n):
    if n==0:
        return("00")
    elif n<10:
        return "0"+str(n)
    else:
        return n


d, a = divmod(int(q), 100)
print(f"{d}.{t(a)}")
