a,b,c = map(int,input().split())
while a or b or c:
    if a and b and c/b == b/a:
        print("GP {}".format(c*(c//b)))
    else:
        print("AP {}".format(2*c-b))
    a,b,c = map(int,input().split())
