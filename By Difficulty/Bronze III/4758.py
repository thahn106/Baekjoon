s,w,p = map(float,input().split())
while int(s) or int(w) or int(p):
    ans = []
    if s<=4.5 and w>=150 and p>=200:
        ans.append("Wide Receiver")
    if s<=6.0 and w>=300 and p>=500:
        ans.append("Lineman")
    if s<=5.0 and w>=200 and p>=300:
        ans.append("Quarterback")
    if ans:
        print(*ans)
    else:
        print("No positions")
    s,w,p = map(float,input().split())
