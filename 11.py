height=[1,7,2,5,12,3,500,500,7,8,4,7,3,6]

l = 0
r = len(height)-1
num = 0
result = 0
length = 0

while l < r:
    if height[l] >= num:
        num = height[l]
        temp = 0
        temp_length = 0
        for n in range(r, l-1, -1):
            print(r, l)
            print(n)
            if height[n] > num:
                pass
            else:
                temp_length = max(temp_length, n-l)
                if temp_length > length:
                    length = temp_length
                    result = height[n] * height[n]
                    result = max(result,temp)
    l += 1

print(result)

            


