n = int(input())
s = []
for i in range(n):
    s.append(int(input()))

arr1 = []
arr2 = []

arr1.append(s[0])
arr2.append(s[1])

for i in range(2,n):
    if arr1[-1] > arr2[-1]:
        arr1.append(s[i])

    else:
        arr2.append(s[i])

ans = arr1 + arr2

print(ans)