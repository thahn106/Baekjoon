N = int(input())
files = []
for i in range(N):
    files.append(input())
M = len(files[0])
ans = ""
for i in range(M):
    chars = [file[i] for file in files]
    if min(chars) == max(chars):
        ans += chars[0]
    else:
        ans += "?"
print(ans)
