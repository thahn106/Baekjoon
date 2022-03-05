N, M = map(int, input().split())
st = []
for i in range(N):
    n = int(input())
    st.insert(n-1, i+1)

st = st[:M]
st.reverse()
f = []
for i in st:
    n = int(input())
    f.insert(n-1, i)
print(f[0])
print(f[1])
print(f[2])
