class Solution:
    def search(self, nums, target: int) -> bool:
        l = int(0)
        r = int(len(nums) - 1)
        while (l<=r):
            mid = int(l+(r-l)/2)
            if(nums[mid]==target):
                return True
            if(nums[l]==nums[mid]):
                l += 1
            elif(nums[mid]<=nums[r]):
                if(target>nums[mid] and target<=nums[r]):
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if(target>=nums[l] and target<nums[mid]):
                    r = mid - 1
                else:
                    l = mid + 1
        return False

nums = [2,5,6,0,0,1,2]
target = 2
ss = Solution()
s=ss.search(nums,target)
print(s)