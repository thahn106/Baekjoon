import sys
input = sys.stdin.readline

for q in range(int(input())):
    a = int(input())
    sys.stdout.write(str(int((a&(-a)) == a))+'\n')
