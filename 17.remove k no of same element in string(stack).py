s = str(input())

k = int(input())
st = []

for ch in s:
    if st and st[-1][0] == ch:
        st[-1][1] += 1
    else:
        st.append([ch,1])

    if st[-1][1] == k:
        st.pop()

res = ""

for ch,count in st:
    res += ch*count

print(res)
