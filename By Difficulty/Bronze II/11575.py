import sys
for t in range(int(input())):
    a, b = map(int, input().split())
    a = a % 26
    b = b % 26
    ans = ""
    ref = ['A']*26
    for i in range(26):
        ref[i] = chr(((a*(i)+b) % 26)+65)
    for c in input():
        sys.stdout.write(ref[ord(c)-65])
    sys.stdout.write('\n')
    sys.stdout.flush()
