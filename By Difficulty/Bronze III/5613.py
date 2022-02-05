s = int(input())
op = input()
while op!="=":
    if op == "+":
        s += int(input())
    elif op == "-":
        s -= int(input())
    elif op == "*":
        s *= int(input())
    elif op == "/":
        s = s//int(input())
    op = input()
print(s)
