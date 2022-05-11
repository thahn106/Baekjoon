A = sum(list(map(int, input().split())))
B = sum(list(map(int, input().split())))
if A>B:
    print("Gunnar")
elif B>A:
    print("Emma")
else:
    print("Tie")
