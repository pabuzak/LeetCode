heights=[1,2,4,3]

l = 0
r = len(heights)
result = 0
num = 0
    

while l < r:
    num = heights[l]
    for n in range(l, r):
        if heights[n] > num:
            pass
        else:
            length = n-l
            result = max(result,heights[n] * length)
    l += 1

print(result)

            


