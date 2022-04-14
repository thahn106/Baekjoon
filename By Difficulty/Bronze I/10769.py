s = input()
happy = s.count(':-)')
sad = s.count(':-(')
if not (happy or sad):
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
else:
    print("sad")
