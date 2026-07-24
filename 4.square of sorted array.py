n = int(input())
arr = []
for i in range(n):
    
    arr.append(int(input()))

pos = []
neg = []

for i in range(len(arr)):
    if arr[i] < 0:
        neg.append(arr[i]*arr[i])
        neg.reverse()
    else:
        pos.append(arr[i]*arr[i])

if len(neg) == 0:
    print(pos)
elif len(pos) == 0:
    print(neg)
else:
    i , j = 0, 0
    idx = 0
    while i < len(neg) and j < len(pos):
        if neg[i] <= pos[j]:
            arr[idx] = neg[i]
            i += 1
            idx += 1

        else:
            arr[idx] = pos[j]
            j += 1
            idx += 1

    while i < len(neg):
        arr[idx] = neg[i]
        idx += 1
        i += 1

    while j < len(pos):
        arr[idx] = pos[j]
        idx += 1
        j += 1

print(arr)
        