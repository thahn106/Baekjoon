A = 0
for i in range(3):
    A += (3-i)*int(input())

B = 0
for i in range(3):
    B += (3-i)*int(input())

if A>B:
    print("A")
elif B>A:
    print("B")
else:
    print("T")
