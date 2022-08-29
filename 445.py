# 有一群孩子和一堆饼干，每个孩子有一个饥饿度，每个饼干都有一个大小。
# 每个孩子只能吃 一个饼干，且只有饼干的大小不小于孩子的饥饿度时，
# 这个孩子才能吃饱。求解最多有多少孩子 可以吃饱。

class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        child = 0
        cookie = 0
        def checkList (g):
            i = 0
            for n in g:
                if n != 0:
                    i = i + 1
            return i
        def checkList (s):
            j = 0
            for n in s:
                if n != 0:
                    j = j + 1
            return j
        while(child < checkList(g) and cookie < checkList(s)):
            if g[child]<=s[cookie]:
                child = child + 1
            cookie = cookie + 1
        return child

g = [1,2,3]
s = [1,2]
ss = Solution()
sss=ss.findContentChildren(g,s)
print(sss)

