from math import ceil

S = int(input())
A = int(input())
B = int(input())

print(250+100*ceil(max(0,S-A)/B))
