class Solution(object):
    def containsDuplicate(self, nums):
        distinct_nums = []

        for n in range(len(nums)-1, -1, -1):
            if nums[n] in distinct_nums:
                return True
            distinct_nums.append(nums[n])
        
        return False
            
        
s = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
duplicate = s.containsDuplicate(nums)
print(duplicate)

nums = [1,2,3,4]
duplicate = s.containsDuplicate(nums)
print(duplicate)

nums = [3,3]
duplicate = s.containsDuplicate(nums)
print(duplicate)