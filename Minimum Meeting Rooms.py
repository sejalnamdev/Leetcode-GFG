n = int(input())
start = []

for i in range(n):
    start.append(int(input()))

m = int(input())
end = []

for i in range(m):
    end.append(int(input()))

start.sort()
end.sort()

i, j = 0, 0
rooms = 0
res = 0

while i < len(start) and j < len(end):
    if start[i] < end[j]:
        rooms += 1
        res = max(res, rooms)
        i += 1
    else:
        rooms -= 1
        j += 1

print(res)