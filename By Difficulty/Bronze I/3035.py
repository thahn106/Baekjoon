R, C, ZR, ZC = map(int, input().split())

for r in range(R):
    row = ""
    for c in input():
        row += c*ZC
    for zr in range(ZR):
        print(row)
