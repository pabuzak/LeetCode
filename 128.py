nums=[9,1,4,7,3,-1,0,5,8,-1,6]

seq = set(nums)
num = 0
max_count = 0

for n in seq:
    if n-1 not in seq:
        count = 1
        num = n
        for n in seq:
            if num+1 in seq:
                count += 1
            else:
                break

        max_count = max(count, max_count)

print(max_count)