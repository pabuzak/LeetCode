nums = [0, 1, 0, 3, 12]
### if 0, find next non zero number, then swap
i = 0

while i < len(nums):

    if nums[i] == 0:
        for j in range(i, len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                break

    i += 1

print(nums)
