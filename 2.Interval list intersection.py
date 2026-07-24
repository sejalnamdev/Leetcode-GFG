n = int(input())
firstList = []  
for i in range(n):
    start, end = map(int, input().split())
    firstList.append([start, end])

m = int(input())
secondList = []
for i in range(m):
    start, end = map(int, input().split())
    secondList.append([start, end])

res = []
i = 0
j = 0
while i < len(firstList) and j < len(secondList):
            
            start1 = firstList[i][0]
            end1 = firstList[i][1]

            start2 = secondList[j][0]
            end2 = secondList[j][1]

            if start1 <= start2:
                if end1 >= start2:
                    s = max(start1, start2)
                    e = min(end1, end2)
                    res.append([s,e])

            else:
                if end2 >= start1:
                    s = max(start1, start2)
                    e = min(end1, end2)
                    res.append([s,e])

            if end1 <= end2:
                i += 1
            else:
                j += 1

print(res)