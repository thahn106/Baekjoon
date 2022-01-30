M = int(input())
D = int(input())
S = 2*31+18
if M*31+D < S:
    print("Before")
elif M*31+D > S:
    print("After")
else:
    print("Special")
