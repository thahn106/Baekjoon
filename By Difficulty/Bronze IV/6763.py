L = int(input())
S = int(input())
if S<=L:
    print("Congratulations, you are within the speed limit!")
elif S<=L+20:
    print("You are speeding and your fine is $100.")
elif S<=L+30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")
