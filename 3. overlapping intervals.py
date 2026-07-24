n = int(input())
arr = []
for i in range(n):
    start, end = map(int, input().split())
    arr.append([start, end])

start1 = arr[0][0]
end1 = arr[0][1]
for i in range(1, len(arr)):
    start2 = arr[i][0]
    end2 = arr[i][1]
    if start2 <= end1:
        print(True)
    start1 = start2
    end1 = max(end1, end2)
if not True:
    print(False)