from tabnanny import check


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        l, r, target = 0, len(nums) - 1, len(nums) - k
        while l < r:
            mid = quicksort(nums, l, r)
            if mid == target:
                return nums[mid]
            elif mid < target:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]


def quicksort(nums, l, r):
    i, j = l + 1, r
    while True:
        while i < r and nums[i] <= nums[l]:
            i += 1
        while l < j and nums[j] >= nums[l]:
            j -= 1
        if i >=j:
            break
        nums[i], nums[j] = nums[j], nums[i]
    nums[l], nums[j] = nums[j], nums[l]
    return j

g = [3,2,1,5,6,4]
s = 3
ss = Solution()
sss=ss.findKthLargest(g,s)
print(sss)