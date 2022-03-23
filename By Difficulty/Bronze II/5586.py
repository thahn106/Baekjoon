s = input()
J = 0
I = 0
for i in range(len(s)-2):
    if s[i:i+3]=='JOI':
        J+=1
    elif s[i:i+3]=='IOI':
        I+=1
print(J)
print(I)
