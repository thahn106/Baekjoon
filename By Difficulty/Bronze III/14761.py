X,Y,N = map(int,input().split())
for i in range(1,N+1):
    if i%X and i%Y:
        print(i)
    elif i%X:
        print('Buzz')
    elif i%Y:
        print('Fizz')
    else:
        print('FizzBuzz')
