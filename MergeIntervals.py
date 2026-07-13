class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()                        #sort from the start
        start1 = intervals[0][0]
        end1 = intervals[0][1]

        for i in range(1, len(intervals)):
            start2 = intervals[i][0]
            end2 = intervals[i][1]

            if end1 >= start2:                  #overlapping then merge it
                start1 = start1
                end1 = max(end1, end2)

            else:                               #no overlapping
                res.append([start1, end1])

                start1 = start2                 #update
                end1 = end2

        res.append([start1, end1])              #last interval

        return res