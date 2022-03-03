R,C = map(int,input().split())
A,B = map(int,input().split())

ref = "X."
start = 0
for x in range(R):
    i = start
    row = ""
    for y in range(C):
        row += ref[i]*B
        i = 1-i
    for a in range(A):
        print(row)
        
    start = 1-start