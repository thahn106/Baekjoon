n = input()
while n != 'EOI':
    found = False
    for i in range(len(n)-4):
        if n[i:i+4].lower() == 'nemo':
            found = True
            break
    if found:
        print("Found")
    else:
        print("Missing")
    n = input()
