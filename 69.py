class Solution:
    def mySqrt(self, x: int) -> int:
        if(x == 0):
            return x
        l = int(1)
        r = x
        while(l<=r):
            mid = int(l + (r-l)/2)
            sqrt = int(x / mid)
            if(sqrt == mid):
                return sqrt
            elif(sqrt > mid):
                l = mid + 1
            else:
                r = mid - 1
        return r