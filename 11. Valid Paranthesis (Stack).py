s = input()
st = []

pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

for ch in s:
    if ch in "([{":
        st.append(ch)

    else:
        if not st or st[-1] != pairs[ch]:
            print(False)
        st.pop()

if not st :
    print(True)
else:
    print(False)
