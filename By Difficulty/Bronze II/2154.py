N = int(input())
s = ""
for i in range(N):
    s += str(i+1)

w = str(N)

for i in range(len(s)-(len(w)-1)):
    if s[i:i+len(w)]==w:
        print(i+1)
        break
