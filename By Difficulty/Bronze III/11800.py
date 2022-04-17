ref = ["Yakk", "Doh", "Seh", "Ghar", "Bang", "Sheesh"]
ref2 = ["Habb Yakk", "Dobara", "Dousa", "Dorgy", "Dabash", "Dosh"]
for t in range(int(input())):
    a, b = map(int, input().split())
    a, b = max(a, b), min(a, b)
    if a == b:
        ans = ref2[a-1]
    elif a == 6 and b == 5:
        ans = "Sheesh Beesh"
    else:
        ans = ref[a-1] + ' ' + ref[b-1]
    print(f"Case {t+1}: {ans}")
