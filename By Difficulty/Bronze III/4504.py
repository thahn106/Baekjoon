n =int(input())
a = int(input())
while a:
    st = ""
    if a%n:
        st = "NOT "
    print("{} is {}a multiple of {}.".format(a, st, n))
    a = int(input())
