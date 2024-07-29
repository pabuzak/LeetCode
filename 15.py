nums = [-1,0,1,2,-1,-4]

l = 0
r = len(nums)-1
results = set()

while l < r:
    result = set()
    for j in range(l+1, r):
        if l != j and l != r and j != r:
            three_sum = nums[l] + nums[j] + nums[r]
            if three_sum == 0:
                sort_result = sorted([nums[l], nums[j], nums[r]])

                results.add(tuple(sort_result))       
                    
    if r-1 == l and l != len(nums)-1:
        r = len(nums)-1
        l += 1
    else:
        r-=1
    
my_list = [list(item) for item in results]
print(my_list)


