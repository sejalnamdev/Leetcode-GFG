ransomNote = str(input())
magazine = str(input())

have = {}

for ch in ransomNote:
    have[ch] = have.get(ch,0) + 1

need = {}

for key in magazine:
    need[key] = need.get(key,0) + 1

for text in have:
    if need.get(text,0) < have[text]:
        print(False)
        

print(True)