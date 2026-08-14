n = int(input())
s = []

for i in range(n):
    s.append(int(input()))

res = [-1]*n
st = []

for i in range(n-1, -1, -1):
    while st and st[-1] <= s[i]:
        st.pop()

    if st :
        res[i] = st[-1]

    st.append(s[i])

print(res) 

