s = str(input())

mp = {}

for ch in s:
    mp[ch] = mp.get(ch,0) + 1

res = 0
odd = False

for ch in mp:
    if mp[ch] % 2 == 0:
        res += mp[ch]

    else:
        res += mp[ch] - 1
        odd = True

if odd:
    res += 1

print(res)