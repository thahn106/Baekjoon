import sys
of = set()
for t in range(int(input())):
    a,b = sys.stdin.readline().split()
    if b == 'enter':
        of.add(a)
    else:
        of.remove(a)
for name in sorted(list(of), reverse=True):
    sys.stdout.write(name+'\n')
sys.stdout.flush()
