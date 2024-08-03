heights=[1,7,2,5,12,3,500,500,7,8,4,7,3,6]

l = 0
r = len(heights)-1
num = 0
result = 0
length = 0

while l < r:
    if heights[l] >= num:
        num = heights[l]
        temp = 0
        for n in range(r, l-1, -1):
            print(heights[n])
            if heights[n] > num:
                pass
            else:
                temp_length = n-l
                if temp_length > length:
                    length = temp_length
                    result = heights[n] * length
                    result = max(result,temp)
    l += 1
            

        
    l += 1

print(result)

            


