import math

piles=[3,6,7,11]
h=8

left = 1
right = max(piles)
mid = (right+left)//2
k = mid

result = float('inf')

while(left <= right):
    
    total_hours = 0

    for i in range(len(piles)):
        num_of_bananas = piles[i]
        ## if mod is true, returns 1 and adds 1
        total_hours += int(num_of_bananas / mid) + (num_of_bananas % mid > 0)
            
    if total_hours <= h:
        right = k-1
        mid = (right+left)//2
        if k < result:
            result = k
        k = mid    
    else:
        left = k+1
        mid = (right+left)//2
        k = mid

print(result)
        