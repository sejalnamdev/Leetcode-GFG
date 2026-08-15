n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

st = []
res = [0]*n

for i in range(n-1,-1,-1):
    while st and a[st[-1]] <= a[i]:
        st.pop()

    if st:
        res[i] = st[-1] - i

    st.append(i)

print(res)