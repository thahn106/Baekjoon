N = int(input())
strings = []
for i in range(N):
    s = input()
    strings.append((len(s),s))
strings = list(set(strings))
strings.sort()
for row in strings:
    print(row[1])
