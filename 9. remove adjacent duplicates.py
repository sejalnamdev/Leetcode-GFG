s = str(input())
st = []
res = []

for i in range(len(s)):
    if not st:
        st.append(s[i])
        continue
    if st[-1] == s[i]:
        st.pop()
        continue
    st.append(s[i])

while st:
    res.append(st.pop())

res.reverse()

print("".join(res))