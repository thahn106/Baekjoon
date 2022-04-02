A = list(input())
B = list(input())
AND = ""
OR = ""
XOR = ""
NA = ""
NB = ""

for a,b in zip(A,B):
    a,b = int(a),int(b)
    AND+=str(int(a and b))
    OR +=str(int(a or b))
    XOR+=str(int(a^b))
    NA+=str(1-a)
    NB+=str(1-b)

print(AND)
print(OR)
print(XOR)
print(NA)
print(NB)
