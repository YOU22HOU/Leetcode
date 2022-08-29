class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        count = 0
        for j in flowerbed:
            count = count + 1
        i = 0
        av = 0
        to_insert = 0
        newflowerbed = [to_insert] + flowerbed
        newflowerbed.append(0)
        while i <= count-1:
            if newflowerbed[i] == 0 and newflowerbed[i+1] == 0 and newflowerbed[i+2] == 0:
                av = av + 1
                newflowerbed[i+1] = 1
            i = i + 1
        return bool(av >= n)

flowerbed = [0,0,0]
n = 2
ss = Solution()
s=ss.canPlaceFlowers(flowerbed,n)
print(s)