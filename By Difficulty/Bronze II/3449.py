for t in range(int(input())):
    a = input()
    b = input()
    ans = 0
    for x,y in zip(a,b):
        if x!=y:
            ans+=1
    print(f"Hamming distance is {ans}.")
    
