nums = [-1,-2,-3,-4,-5]
target = -8

pointer = 0
length = len(nums)

output = set()

for n in range(length-1):
    if (nums[n] + nums[n+1]) == target:
        output.add(n)
        output.add(n+1)

if not output:
    while length > 0:
        for n in range(len(nums)):
            if pointer != n:
                if (nums[pointer] + nums[n]) == target:
                    output.add(pointer)
                    output.add(n)
        pointer += 1
        length -= 1

print(list(output))



### optimised code
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         numToIndex = {}
#         for i in range(len(nums)):
#             if target - nums[i] in numToIndex:
#                 return [numToIndex[target - nums[i]], i]
#             numToIndex[nums[i]] = i
#         return []