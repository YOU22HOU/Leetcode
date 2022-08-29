class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        rintervals = sorted(intervals, key=lambda x:x[1])
        front = 0
        latter = 1
        remove = 0
        n = 0
        for l in intervals:
            n = n + 1
        while(latter < n):
            if rintervals[front][1] > rintervals[latter][0]:
                remove = remove + 1
                latter = latter + 1
            else:
                front = latter
                latter = latter + 1
        return remove

g = [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]
ss = Solution()
s=ss.eraseOverlapIntervals(g)
print(s)