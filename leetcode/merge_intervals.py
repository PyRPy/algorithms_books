# merge_intervals.py
class Solution:
    def merge(self, intervals):
        result  = []
        intervals.sort(key=lambda x:x[0])

        i = 0 
        while i < len(intervals):
            cur_start = intervals[i][0]
            cur_end = intervals[i][1]
            if result:
                prev_start, prev_end = result[-1]
                hi = min(prev_end, cur_end)
                lo = max(prev_start, cur_start)

                if lo <= hi:
                    if cur_end > prev_end:
                        result[-1][1] = cur_end 
                else:
                    result.append(intervals[i])
            else:
                result.append(intervals[i])
            i += 1 
        return result 

intervals = [[1, 4], [4, 5]]
sol = Solution()
print(intervals)
print(sol.merge(intervals))