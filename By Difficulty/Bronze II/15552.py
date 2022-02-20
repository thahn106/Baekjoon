import sys
input = sys.stdin.buffer.readline
from bisect import bisect_left

for t in range(int(input())):
    A,B = map(int,input().strip().split())
    sys.stdout.write(f"{A+B}\n")
sys.stdout.flush()
