nums = [-1,0,1,2,-1,-4]
nums.sort()


j = 0
results = []


# l needs to increase, every loop
# r needs to reset to len(nums)-1 every loop and also decrement
for r in range(len(nums)-1,-1,-1):
    l = 0
    while l < len(nums):
        if l != j and l != r and j != r:
            three_sum = nums[l] + nums[j] + nums[r]
            if three_sum == 0:
                sort_result = sorted([nums[l], nums[j], nums[r]])
                if sort_result not in results:
                    results.append(sort_result)
        l += 1
    j += 1


print(results)


