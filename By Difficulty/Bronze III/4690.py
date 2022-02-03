from math import pow
for a in range(6,101):
    for b in range(2,a):
        for c in range(b,a):
            d3 = a**3-b**3-c**3
            if d3>= c**3:
                d = round(pow(d3,1/3))
                if d**3+c**3+b**3==a**3:
                    print("Cube = {}, Triple = ({},{},{})".format(a,b,c,d))
