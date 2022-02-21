N = int(input())
for i in range(N):
    b = N//2
    t = b+(N%2)
    print("*"+" *"*(t-1))
    if N>1:
        print(" *"*b)
