G,S,C = map(int,input().split())
ans = G*3+S*2+C
if ans<2:
    print("Copper")
elif ans ==2:
    print('Estate or Copper')
elif ans < 5:
    print('Estate or Silver')
elif ans == 5:
    print('Duchy or Silver')
elif ans < 8:
    print("Duchy or Gold")
else:
    print("Province or Gold")
