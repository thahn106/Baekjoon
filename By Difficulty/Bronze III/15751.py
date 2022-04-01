a,b,x,y = map(int,input().split())
print(min(abs(b-a),abs(a-x)+abs(b-y),abs(a-y)+abs(x-b)))
