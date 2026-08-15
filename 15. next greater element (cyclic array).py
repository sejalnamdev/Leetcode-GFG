n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

res = [-1]*n
st = []

for i in range(2*n-1, -1, -1):
    while st and st[-1] <= a[i%n]:
        st.pop()

    if i< n:
        if st:
            res[i] = st[-1]

    st.append(a[i%n])

print(res)


