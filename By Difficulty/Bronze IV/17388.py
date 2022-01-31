A = list(map(int,input().split()))
if sum(A)>=100:
    print("OK")
elif min(A)==A[0]:
    print("Soongsil")
elif min(A)==A[1]:
    print("Korea")
elif min(A)==A[2]:
    print("Hanyang")
