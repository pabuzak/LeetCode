nums = [-1,0,1,2,-1,-4]

l = 0
r = len(nums)-1
results = []

while l < r:
    for j in range(len(nums)):
        if l != j and l != r and j != r:
            three_sum = nums[l] + nums[j] + nums[r]
            print(three_sum)
            if three_sum == 0:
                result = sorted([nums[l], nums[j], nums[r]])

                if result not in results:
                    results.append(result)                
            
    if r-1 == l and l != len(nums)-1:
        r = len(nums)-1
        l += 1
    else:
        r-=1
    
        
print(results)


